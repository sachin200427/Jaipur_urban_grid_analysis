# Urban Heat Island Effect vs. Jaipur Energy Grid

## Project Overview
This project investigates the correlation between the Urban Heat Island (UHI) effect and power grid strain in Jaipur, Rajasthan. By analyzing temperature data and energy consumption patterns, this project identifies critical temperature thresholds that impact infrastructure, utilizes predictive machine learning to forecast future grid stress, and deploys an interactive web dashboard for real-time forecasting.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, Streamlit
* **Core Concepts:** Data Engineering, Statistical Normalization, Data Visualization, Machine Learning (Linear Regression), Frontend Web Development
* **Version Control:** Git & GitHub

## Key Insights
* **Critical Threshold:** Exploratory data analysis reveals a significant spike in grid load once the maximum daily temperature exceeds **42°C**.
* **Data Engineering:** Successfully processed 3 years of synthetic historical data to simulate real-world infrastructure stress and handled intentional missing values.
* **Predictive Forecasting:** A Scikit-Learn Linear Regression model successfully predicts future strain, forecasting a critical surge to **2635.52 MW** if summer temperatures reach **48°C**.
* **Interactive UI:** Built a live Streamlit web application allowing users to input hypothetical extreme temperatures and receive instant load forecasts and risk assessments.

## How to Run
1. Clone this repository: `git clone https://github.com/sachin200427/Jaipur_urban_grid_analysis.git`
2. Run `generate_data.py` to recreate the raw dataset.
3. Open `data_analysis_file.ipynb` in VS Code to see the cleaning process and exploratory visualizations.
4. Open `predictive_modeling.ipynb` to view the machine learning model training, accuracy testing, and future load predictions.
5. Launch the interactive dashboard by running `python -m streamlit run dashboard.py` in your terminal.
