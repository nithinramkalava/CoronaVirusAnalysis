"""Formatted the Data and stored in updated data for easier processing later"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

total_cases = pd.read_csv("Data/time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv("Data/time_series_covid19_deaths_global.csv")
recovered = pd.read_csv("Data/time_series_covid19_recovered_global.csv")

total_cases = total_cases.drop(["Province/State", "Lat", "Long"], axis=1)
deaths = deaths.drop(["Province/State", "Lat", "Long"], axis=1)
recovered = recovered.drop(["Province/State", "Lat", "Long"], axis=1)

total_cases = total_cases.groupby("Country/Region").aggregate(np.sum).transpose()
deaths = deaths.groupby("Country/Region").aggregate(np.sum).transpose()
recovered = recovered.groupby("Country/Region").aggregate(np.sum).transpose()

# print(total_cases)
# print(deaths)
# print(recovered)

relative_cases = total_cases.copy()

for day in range(1, len(total_cases)):
    relative_cases.iloc[day] = total_cases.iloc[day] - total_cases.iloc[day - 1]

growth_rate = total_cases.copy()

for day in range(1, len(total_cases)):
    growth_rate.iloc[day] = total_cases.iloc[day] * 100 / total_cases.iloc[day - 1]

active_cases = total_cases.copy()

for day in range(0, len(total_cases)):
    active_cases.iloc[day] = total_cases.iloc[day] - deaths.iloc[day] - recovered.iloc[day]

total_cases.to_csv("UpdatedData/TotalCases.csv")
deaths.to_csv("UpdatedData/Deaths.csv")
recovered.to_csv("UpdatedData/Recovered.csv")

