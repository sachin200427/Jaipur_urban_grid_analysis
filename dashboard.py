import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Jaipur Grid Dashboard", layout="wide")
st.title("⚡ Jaipur Urban Grid & Heat Island Analysis")

# 2. Load Data and Train Model
@st.cache_data # This makes the dashboard load faster
def load_data():
    return pd.read_csv('jaipur_cleaned_energy_data.csv')

df = load_data()
X = df[['Max_Temp_C']]
y = df['Grid_Load_MW']
model = LinearRegression()
model.fit(X, y)

# 3. Create Tabs for the Dashboard
tab1, tab2 = st.tabs(["📊 Exploratory Analysis", "🤖 Predictive ML Model"])

with tab1:
    st.header("Historical Grid Data")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(df))
    col2.metric("Critical Temp Threshold", "42°C")
    col3.metric("Max Recorded Load", f"{df['Grid_Load_MW'].max()} MW")
    
    st.subheader("Temperature vs. Grid Load")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df['Max_Temp_C'], df['Grid_Load_MW'], alpha=0.5, color='blue')
    ax.axvline(x=42, color='red', linestyle='--', label='42°C Threshold')
    ax.set_xlabel("Max Temperature (°C)")
    ax.set_ylabel("Grid Load (MW)")
    ax.legend()
    st.pyplot(fig)

with tab2:
    st.header("Future Load Forecaster")
    st.write("Use the slider to predict grid strain during extreme heatwaves.")
    
    # Interactive Slider
    temp_input = st.slider("Select Maximum Daily Temperature (°C):", min_value=35.0, max_value=50.0, value=43.0, step=0.5)
    
    # Predict based on slider
    prediction = model.predict(np.array([[temp_input]]))[0]
    
    st.subheader(f"Predicted Grid Load: **{prediction:.2f} MW**")
    
    # Risk Warning System
    if prediction < 2200:
        st.success("🟢 Normal Operation: Grid is stable.")
    elif 2200 <= prediction < 2450:
        st.warning("🟡 Elevated Strain: Risk of localized power cuts.")
    else:
        st.error("🔴 Critical Risk: High probability of widespread grid failure.")