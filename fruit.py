import matplotlib.pyplot as plt
import pandas as pd

filename = "fruit.csv"
data = pd.read_csv(filename, sep="\t")

o_kind = [6,7,8]
l_kind = [9,10]
m_kind = 2
ms = data[data['ty'] == m_kind]
os = data[data['ty'].isin(o_kind)]
ls = data[data['ty'].isin(l_kind)]

plt.scatter(ms["wi"], ms["hg"], label="Mandarin", color="red")
plt.scatter(os["wi"], os["hg"], label="Orange", color="orange")
plt.scatter(ls["wi"], ls["hg"], label="Lemon", color="yellow")
plt.title("Fruit Dimensions")
plt.ylabel("Height")
plt.xlabel("Width")
plt.legend()
plt.show()