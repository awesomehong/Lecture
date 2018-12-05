import pandas as pd
import numpy as np


population = pd.read_csv("population.csv", index_col = "State")
print(population)


print(population.sort_index().head())


alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
print(alco2009.max())
print(alco2009.min(axis=1))
print(alco2009.sum())


alco = pd.read_csv("niaaa-report.csv", index_col=["State", "Year"])

alco["Total"] = alco.Wine + alco.Spirits + alco2009
print(alco.head())

alco_noidx = alco.reset_index()
sum_alco = alco_noidx.groupby("Year").count()
print(sum_alco.tail())

wine_state = alco2009["Wine"] > alco2009["Wine"].mean()
beer_state = alco2009["Beer"] > alco2009["Beer"].mean()
pd.crosstab(wine_state, beer_state)

dna = "AGTCCGCGAATACAGGCTCGGT"
dna1 = dna.replace("C", "")
dna2 = dna.replace("T", "")
dna_as_series1 = pd.Series(list(dna1), name="genes")
dna_as_series2 = pd.Series(list(dna2), name="genes")
dna_as_series1.value_counts() + dna_as_series2.value_counts()