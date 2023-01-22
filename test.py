import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


growth_rate = pd.read_csv("overall_growth_rate.csv",index_col=0)

plt.bar(growth_rate.India[50:70].index,growth_rate.India.iloc[50:70])
plt.show()
