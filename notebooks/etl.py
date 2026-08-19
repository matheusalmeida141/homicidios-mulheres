# %%
import pandas as pd

df = pd.DataFrame()
for i in range(2011, 2026):
    df2 = pd.read_csv(f"../data/violencia-mulher-{i}.csv",)

    df = pd.concat([df, df2])

del df2

df2 = pd.read_csv("../data/homicidios-mulher-ipea.csv")

df.groupby(["idDelito", "delito"])["total"].sum() #id = 58, 134

dfH = df[(df['idDelito'] == 58) | (df['idDelito'] == 134)]

dfH.to_csv("../data/homicidios-ssp.csv", index=False)

# %%
dfH = dfH.groupby(["ano"])[["total"]].sum()

dfH = dfH.reset_index()

dfH["origem"] = "ssp"

df2 = df2.drop(columns=["Região ID"])

df2['origem'] = "ipea"


df2.rename(columns={"Período":"ano", "Valor":"total"}, inplace=True)
dfH = pd.concat([dfH, df2], axis=0)
dfH.reset_index(inplace=True)
dfH.to_csv("../data/homicidios.csv", index=False)
# %%

import pandas as pd

df = pd.read_csv("../data/finlandia.csv")
df = df[["Data","Homicídiosmulheres"]]

df.rename(columns={
    "Homicídiosmulheres": "homicidios"
}, inplace = True)

df.to_csv("../data/fin-homicidios.csv", index=False)
# %%
