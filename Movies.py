import pandas as pd
import heapq
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("imdb5000.csv")

act = list(df.actor_1_name)+list(df.actor_2_name)+list(df.actor_3_name)
act_set = set(act)
act_profit=dict()

for i in range(len(df["movie_title"])):
    df["profit"] = df.gross - df.budget
    
for name in act_set:
    df_sort = df.loc[((df.actor_1_name == name) | (df.actor_2_name == name) | (df.actor_3_name == name))]
    prof = df_sort.profit.sum(axis=0)
    act_profit[name] = prof

top_acts = heapq.nlargest(5, act_profit, key = act_profit.get)

top_num_acts = []
for k in top_acts:
    top_num_acts.append("{0:,.0f}".format(act_profit[k]))
    
print("Top Actors:")
for num in range(5):
    print(f"#{num+1}. {top_acts[num]}: ${top_num_acts[num]}")