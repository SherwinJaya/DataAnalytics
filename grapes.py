import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("europe2012ghd.csv")
yr = data['Year'].values.reshape(-1,1)
val = data['Als'].values.reshape(-1,1)

tenVal = list()
for ww in range(0,len(val)-10): 
    sum = 0.0
    for gg in range(0,10):
        sum = sum + val[(ww+gg)]
    tenVal.append(sum/10)

plt.plot(yr[0:len(tenVal)],tenVal)
plt.show()
