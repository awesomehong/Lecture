import pandas as pd

data = pd.read_csv("lynx.csv")

data["time"] = data.time / 10 

year = round(data.time, 0)
data.time = year * 10

sum_data = data.groupby("time").sum()

result = sum_data.sort_values("value", ascending = false).head()

print(result)