import pandas as pd
from scipy.stats import pearsonr

a = pd.read_csv("GSPC.csv", index_col = "Data")
type(a)
print(a["Close"].mean())
print(pearsonr(a["Close"], a["Volume"]))