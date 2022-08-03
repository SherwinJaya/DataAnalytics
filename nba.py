import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("NBA_head_coaches.csv")

plt.scatter(df["Name"], df["Years"], color = 'blue')
plt.xlabel('Name')
plt.ylabel('Number of Years of Experience')
plt.title('Number of Years Coached in NBA for Every Coach', fontsize = 20)
  
plt.show()