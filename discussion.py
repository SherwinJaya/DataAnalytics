import numpy as np
import pandas as pd
import datetime
from scipy import optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

lynx = pd.read_csv('lynx.csv')
print(lynx.columns)

ltime = lynx['time'].values
xl = list()
for ii in range(0, len(ltime)):
    xl.append((ltime[ii] - ltime[0]))

yl = lynx['value']
yl = yl.tolist()


def my_sin(x_sin, freq, amp, phase, offset):
    return (np.sin(x_sin * freq + phase) * amp + offset)


xl = np.asarray(xl)
yl = np.asarray(yl)

po = [.66, 1100, 15, 1700]
fit = curve_fit(my_sin, xl, yl, p0=po)

data_guess = my_sin(xl, *po)
data_fit = my_sin(xl, *fit[0])

plt.figure(figsize=(12, 5))
plt.plot(xl, yl, 'o')
plt.plot(xl, data_fit, label="fit", color="red")
plt.plot(xl, data_guess, label="guess", color="green")
plt.legend()
plt.show()