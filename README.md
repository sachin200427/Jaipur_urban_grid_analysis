# Urban Heat Island Effect vs. Jaipur Energy Grid

## Project Overview
This project investigates the correlation between the Urban Heat Island (UHI) effect and power grid strain in Jaipur, Rajasthan. By analyzing temperature data and energy consumption patterns, this project identifies critical temperature thresholds that impact infrastructure and utilizes predictive machine learning to forecast future grid stress.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn
* **Core Concepts:** Data Cleaning, Statistical Normalization, Data Visualization, Machine Learning (Linear Regression)
* **Version Control:** Git & GitHub

## Key Insights
* The exploratory data analysis reveals a significant spike in grid load once the maximum daily temperature exceeds **42°C**.
* The project successfully processed 3 years of synthetic historical data to simulate real-world infrastructure stress.
* **Predictive Forecasting:** A Scikit-Learn Linear Regression model successfully predicts future strain, forecasting a critical surge to **2635.52 MW** if summer temperatures reach **48°C**.

## How to Run
1. Clone this repository: `git clone https://github.com/sachin200427/Jaipur_urban_grid_analysis.git`
2. Run `generate_data.py` to recreate the raw dataset.
3. Open `data_analysis_file.ipynb` in VS Code to see the cleaning process and exploratory visualizations.
4. Open `predictive_modeling.ipynb` to view the machine learning model training, accuracy testing, and future load predictions.
