import pandas as pd

class growth_and_death_rate:
    def __init__(self) -> None:

        confirmed = pd.read_csv("FormattedData/confirmed.csv",index_col=0)
        deaths = pd.read_csv("FormattedData/deaths.csv",index_col=0)
        recovered = pd.read_csv("FormattedData/recovered.csv",index_col=0)


        active_cases = confirmed - recovered - deaths

        growth_rate = active_cases.pct_change() * 100
        death_rate = deaths *100 / confirmed

        growth_rate.to_csv("Rates/growth_rate.csv")
        death_rate.to_csv("Rates/death_rate.csv")
