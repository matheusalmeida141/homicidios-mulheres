# %%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
dfH = pd.read_csv("../data/homicidios.csv")

ax = sns.lineplot(dfH, x="ano", y="total", hue="origem", palette=sns.color_palette("Set2"))
ax.set_title("Homícidios de Mulheres no Estado de São Paulo")
plt.show()


ax = sns.lineplot(dfH, x="ano", y="total", hue="origem", palette=sns.color_palette("Set2"))
ax.set_title("Homícidios de Mulheres no Estado de São Paulo")
ax.set_xlim(dfH[dfH["origem"] == 'ssp']['ano'].min(),
             dfH[dfH["origem"] == "ipea"]['ano'].max())
plt.show()


dfH.drop(columns=["index"], inplace=True)


diff = pd.concat([dfH[(dfH["origem"] == 'ssp') & (dfH['ano'] <= 2023 ) ].set_index("ano"),dfH[(dfH["origem"] == 'ipea') & (dfH['ano'] >= 2011 ) ].set_index("ano") ], axis=1)

diff.columns.values[0] , diff.columns.values[2]= "ssp", "ipea"

diff = diff.drop(columns=["origem"])

diff["diferenca"] = np.abs(diff["ssp"] - diff["ipea"])


plt.figure(dpi=500)
ax = sns.lineplot(diff, x="ano", y="diferenca")
ax.set_title("Diferença entre número de casos entre SSP e IPEA no Estado de SP")
ax.set_ylabel("diferença")
ax.set_xticks(range(2011,2024, 2))
plt.show()


del diff
del dfH


df = pd.read_csv("../data/homicidios-ssp.csv")

df = df.drop(columns=["capital", "demacro", "interior"])
df.head()


#Calculando as médias e os desvios padrões
df.groupby("ano")["total"].describe()


#vendo a distribuição
fig, axes = plt.subplots(nrows= 3, ncols= 5, figsize=(10, 15))

axes = axes.flatten()


for i, j in enumerate(range(2011,2026)):
    axes[i].hist(df[ df["ano"] == j ]['total'], bins = 10 ,color="skyblue", edgecolor="black")
    axes[i].set_title(j)
plt.tight_layout()
plt.show()

plt.hist(df["total"], color="skyblue", edgecolor="black")
plt.title("Contagem de Homicídios de Mulheres durante os anos de 2011 à 2025")
plt.xlabel("Número de homícidios")
plt.ylabel("Frequência")
plt.show()


# %%
#calculando lesão vs homicidio
dfH = df[ (df["idDelito"] != 61)]
dfH = dfH.groupby(["ano"])[["total"]].sum()
dfE = df[ (df["idDelito"] == 68)]
dfE = dfE.groupby(["ano"])[["total"]].sum()
# %%

plt.plot(dfH.index, dfH["total"], label = "Homícidios")
plt.plot(dfE.index, dfE["total"], label = "Estrupo")
plt.title("Homícidios e Estrupo de Mulheres ao longo dos anos")
plt.xlabel("Ano")
plt.ylabel("nº de ocorrência")
plt.legend()
# %%
plt.plot(dfE["total"], dfH["total"], 'o')
plt.title("Homícidios vs Estupro")
plt.xlabel("Estrupos")
plt.ylabel("Homícidios")
print(dfE["total"].corr(dfH["total"]))
# %%
