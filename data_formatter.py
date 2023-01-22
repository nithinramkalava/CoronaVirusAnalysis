import numpy as np
import pandas as pd

class data_formatter:
    def __init__(self) -> None:
        confirmed = pd.read_csv("Data/time_series_covid19_confirmed_global.csv")
        deaths = pd.read_csv("Data/time_series_covid19_deaths_global.csv")
        recovered = pd.read_csv("Data/time_series_covid19_recovered_global.csv")

        confirmed = confirmed.drop(["Province/State", "Lat", "Long"], axis=1)
        deaths = deaths.drop(["Province/State", "Lat", "Long"], axis=1)
        recovered = recovered.drop(["Province/State", "Lat", "Long"], axis=1)

        confirmed = confirmed.groupby("Country/Region").aggregate(np.sum).transpose()
        deaths = deaths.groupby("Country/Region").aggregate(np.sum).transpose()
        recovered = recovered.groupby("Country/Region").aggregate(np.sum).transpose()

        confirmed.index = pd.to_datetime(confirmed.index,dayfirst=True)
        deaths.index = pd.to_datetime(deaths.index,dayfirst=True)
        recovered.index = pd.to_datetime(recovered.index,dayfirst=True)

        confirmed.to_csv("FormattedData/confirmed.csv")
        deaths.to_csv("FormattedData/deaths.csv")
        recovered.to_csv("FormattedData/recovered.csv")
