import pandas as pd
dataTab = pd.read_csv("Rides.csv")
rideNum = dataTab['rides']
[rideNum.max(), rideNum.idxmax()]
stationName = dataTab['stationname'][rideNum.idxmax()]
busyDay = dataTab['date'][rideNum.idxmax()]
stationName