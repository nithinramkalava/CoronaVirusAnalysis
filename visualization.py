import pandas as pd
import matplotlib.pyplot as plt

confirmed = pd.read_csv("UpdatedData/TotalCases.csv")

hospitalization_rate_estimate = 0.05

hospitalization_needed = confirmed.copy()

for day in range(0, len(confirmed)):
    hospitalization_needed.iloc[day] = active_cases.iloc[day] * hospitalization_rate_estimate