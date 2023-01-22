import numpy as np
import pandas as pd


confirmed = pd.read_csv(r"Data\time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv(r"Data\time_series_covid19_deaths_global.csv")
recovered = pd.read_csv(r"Data\time_series_covid19_recovered_global.csv")

confirmed = confirmed.drop(["Province/State", "Lat", "Long"], axis=1)
deaths = deaths.drop(["Province/State", "Lat", "Long"], axis=1)
recovered = recovered.drop(["Province/State", "Lat", "Long"], axis=1)
