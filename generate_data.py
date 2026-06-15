import pandas as pd
import numpy as np
from datetime import timedelta, date

# Generate dates for the last 3 summers in Jaipur
start_date = date(2023, 4, 1)
end_date = date(2026, 6, 27)
dates = pd.date_range(start_date, end_date, freq='D')

# Create realistic Jaipur summer temperatures (Hotter in May/June)
np.random.seed(42)
temperatures = 35 + 10 * np.sin(np.pi * dates.month / 6) + np.random.normal(0, 2, len(dates))

# Create Power Grid Load (spikes when temp goes above 40°C)
base_load = 1500 # Megawatts
power_load = base_load + (temperatures - 30) * 50 + np.random.normal(0, 50, len(dates))
power_load = np.where(temperatures > 42, power_load + 300, power_load) # AC usage spike

# Create the dataframe
df = pd.DataFrame({'Date': dates, 'Max_Temp_C': temperatures, 'Grid_Load_MW': power_load})

# Introduce some fake missing values to prove you know how to "clean" data
df.loc[df.sample(frac=0.05).index, 'Max_Temp_C'] = np.nan 

# Save to CSV
df.to_csv('jaipur_raw_energy_data.csv', index=False)
print("Raw dataset created successfully!")