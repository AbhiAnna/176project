#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
mergedTempCO2Quality = pd.read_csv('mergedTempCO2Quality.csv')
dfHistorical = pd.read_csv('dfHistorical.csv')

# Convert 'Year_x', 'AverageTemperature', and 'CO2 emission (tons)' to numeric
dfHistorical['Year_x'] = pd.to_numeric(dfHistorical['Year_x'], errors='coerce')
dfHistorical['AverageTemperature'] = pd.to_numeric(dfHistorical['AverageTemperature'], errors='coerce')
dfHistorical['CO2 emission (tons)'] = pd.to_numeric(dfHistorical['CO2 emission (tons)'], errors='coerce')


# Sort dfHistorical by 'Year_x'
dfHistorical = dfHistorical.sort_values('Year_x')

# Convert columns to numeric
mergedTempCO2Quality['Year_x'] = pd.to_numeric(mergedTempCO2Quality['Year_x'], errors='coerce')
mergedTempCO2Quality['AverageTemperature'] = pd.to_numeric(mergedTempCO2Quality['AverageTemperature'], errors='coerce')
mergedTempCO2Quality['CO2 emission (Tons)'] = pd.to_numeric(mergedTempCO2Quality['CO2 emission (Tons)'], errors='coerce')
mergedTempCO2Quality['AirQuality'] = pd.to_numeric(mergedTempCO2Quality['AirQuality'], errors='coerce')
mergedTempCO2Quality['WaterPollution'] = pd.to_numeric(mergedTempCO2Quality['WaterPollution'], errors='coerce')


# Sort mergedTempCO2Quality by 'Year_x'
mergedTempCO2Quality = mergedTempCO2Quality.sort_values('Year_x')


# Pivot Table 1: Average CO2 Emission per Year
pivot_co2_year = mergedTempCO2Quality.pivot_table(
    values='CO2 emission (Tons)',
    index='Year_x',
    aggfunc='mean'
).reset_index()

# Pivot Table 2: Average Temperature and CO2 Emission per Decade
# Create 'Decade' column
mergedTempCO2Quality['Decade'] = (mergedTempCO2Quality['Year_x'] // 10) * 10
mergedTempCO2Quality['Decade'] = mergedTempCO2Quality['Decade'].astype(int)

pivot_temp_co2_decade = mergedTempCO2Quality.pivot_table(
    values=['AverageTemperature', 'CO2 emission (Tons)'],
    index='Decade',
    aggfunc='mean'
).reset_index()

# 3. Plotting Graphs

#Graph 1: Historical CO2 Emission (1900 to 2013)
plt.figure(figsize=(10, 6))
plt.plot(dfHistorical['Year_x'], dfHistorical['CO2 emission (tons)'], label='CO2 Emission', color='blue')
plt.title('Historical CO2 Emission (1900 to 2013)')
plt.xlabel('Year')
plt.ylabel('CO2 Emission (tons)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#Graph 2: AverageTemperature vs. CO2 Emission Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(mergedTempCO2Quality['AverageTemperature'], mergedTempCO2Quality['CO2 emission (Tons)'], alpha=0.7, color='green')
plt.title('Average Temperature vs CO2 Emission')
plt.xlabel('Average Temperature')
plt.ylabel('CO2 Emission (Tons)')
plt.grid(True)
plt.tight_layout()
plt.show()

#Graph 3: Distribution of Air Quality Histogram
plt.figure(figsize=(10, 6))
plt.hist(mergedTempCO2Quality['AirQuality'], bins=30, alpha=0.7, color='orange', edgecolor='black')
plt.title('Distribution of Air Quality')
plt.xlabel('Air Quality')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#Graph 4: AverageTemperature and CO2 Emission Over Time
plt.figure(figsize=(10, 6))
plt.plot(mergedTempCO2Quality['Year_x'], mergedTempCO2Quality['AverageTemperature'], label='Average Temperature', color='red')
plt.plot(mergedTempCO2Quality['Year_x'], mergedTempCO2Quality['CO2 emission (Tons)'], label='CO2 Emission', color='blue')
plt.title('Average Temperature and CO2 Emission Over Time')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#Graph 5: Average CO2 Emission by Decade (Bar Plot)
plt.figure(figsize=(10, 6))
plt.bar(pivot_temp_co2_decade['Decade'].astype(str), pivot_temp_co2_decade['CO2 emission (Tons)'], color='purple', alpha=0.7)
plt.title('Average CO2 Emission by Decade')
plt.xlabel('Decade')
plt.ylabel('Average CO2 Emission (Tons)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#Graph 6: Average Temperature and CO2 Emission per Decade
plt.figure(figsize=(10, 6))
plt.plot(pivot_temp_co2_decade['Decade'], pivot_temp_co2_decade['AverageTemperature'], label='Average Temperature', marker='o', color='red')
plt.plot(pivot_temp_co2_decade['Decade'], pivot_temp_co2_decade['CO2 emission (Tons)'], label='Average CO2 Emission', marker='s', color='blue')
plt.title('Average Temperature and CO2 Emission per Decade')
plt.xlabel('Decade')
plt.ylabel('Average Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:




