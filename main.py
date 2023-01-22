"""Formatted the Data and stored in updated data for easier processing later"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

confirmed = pd.read_csv("Data/time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv("Data/time_series_covid19_deaths_global.csv")
recovered = pd.read_csv("Data/time_series_covid19_recovered_global.csv")

confirmed = confirmed.drop(["Province/State", "Lat", "Long"], axis=1)
deaths = deaths.drop(["Province/State", "Lat", "Long"], axis=1)
recovered = recovered.drop(["Province/State", "Lat", "Long"], axis=1)

confirmed = confirmed.groupby("Country/Region").aggregate(np.sum).transpose()
deaths = deaths.groupby("Country/Region").aggregate(np.sum).transpose()
recovered = recovered.groupby("Country/Region").aggregate(np.sum).transpose()

# print(total_cases)
# print(deaths)
# print(recovered)

relative_cases = confirmed.copy()

for day in range(1, len(confirmed)):
    relative_cases.iloc[day] = confirmed.iloc[day] - confirmed.iloc[day - 1]

growth_rate = confirmed.copy()

for day in range(1, len(confirmed)):
    growth_rate.iloc[day] = confirmed.iloc[day] * 100 / confirmed.iloc[day - 1]

active_cases = confirmed.copy()

for day in range(0, len(confirmed)):
    active_cases.iloc[day] = confirmed.iloc[day] - deaths.iloc[day] - recovered.iloc[day]

confirmed.to_csv("UpdatedData/TotalCases.csv")
deaths.to_csv("UpdatedData/Deaths.csv")
recovered.to_csv("UpdatedData/Recovered.csv")

