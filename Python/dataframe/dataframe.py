import pandas as pd
import numpy as np


population = pd.read_csv("population.csv", index_col = "State")
print(population)


print(population.sort_index().head())


alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
print(alco2009.max())
print(alco2009.min(axis=1))
print(alco2009.sum())



dna = "AGTCCGCGAATACAGGCTCGGT"
dna1 = dna.replace("C", "")
dna2 = dna.replace("T", "")
dna_as_series1 = pd.Series(list(dna1), name="genes")
dna_as_series2 = pd.Series(list(dna2), name="genes")
dna_as_series1.value_counts() + dna_as_serires2.value_counts()

dna_as_series.unique()
dna_as_series.value_counts().sort_index()

valid_nucs = list("ACGT")
dna_as_series.isin(valid_nucs).all()