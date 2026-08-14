# %%
import pandas as pd

df = pd.read_csv("../data/homicidios-mulheres-estados.csv")

df["Período"] = pd.to_datetime(df["Período"]).dt.year
# %%

df[ df["Região ID"] == 35]
# %%
