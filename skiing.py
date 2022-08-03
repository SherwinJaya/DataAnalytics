import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

skit = pd.read_csv("multiTimeline.csv")
print(skit.columns)

xall = pd.to_datetime(skit['Month'].values)

xv = list()
for ii in range(0, len(xall)):
    xv.append((xall[ii]-xall[0]).days)

yv = skit['skiing: (United States)']
yv = yv.tolist()

plt.figure(figsize=(12,3))
plt.plot(xv,yv)
plt.show()
from scipy.optimize import curve_fit
def my_sin(x, freq, amp, phase, offset):
    return(np.sin (x * freq + phase) * amp +offset)

yv = np.asarray(yv)
xv = np.asarray(xv)

po = [.017, 20, 365, 90]

fit = curve_fit(my_sin, xv, yv, p0=po)
data_guess = my_sin(xv, *po)
data_fit = my_sin(xv, *fit[0])

plt.figure(figsize=(12,4))
plt.plot(xv,yv,'o')
plt.plot(xv, data_fit, label = "fit")
plt.plot(xv, data_guess, label = "guess")
plt.legend()
plt.show()
