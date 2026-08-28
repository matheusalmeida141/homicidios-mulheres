# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("../data/ssp-feminicidio.csv")
df.head()
# %%

tabela = df.groupby("COR_PELE")[["NUM_BO"]].count().sort_values(by="NUM_BO", ascending=False)
tabela.rename(columns={"NUM_BO": "FrequenciaAbs"}, inplace=True)
tabela["FrequenciaAbsAcumulada"] = tabela["FrequenciaAbs"].cumsum()
tabela["FrequenciaRelativa"] = tabela["FrequenciaAbs"]/tabela["FrequenciaAbs"].sum()
tabela["FrequemcoaRelativaAcumulada"] = tabela["FrequenciaRelativa"].cumsum()
tabela


# %%
sns.histplot(df, x="IDADE_PESSOA")
plt.title("Histograma de vítimas de feminicídio em SP entre 2015 ~ 2022")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.show()
print(df[["IDADE_PESSOA"]].describe())
# %%

df[ df["IDADE_PESSOA"] <= 20].groupby("IDADE_PESSOA")[["NUM_BO"]].count()

# %%

df.groupby("PROFISSAO")[["NUM_BO"]].count().sort_values(by= "NUM_BO", ascending=False)


# %%
tabela = df.groupby("DESC_TIPOLOCAL")[["NUM_BO"]].count().sort_values(by="NUM_BO", ascending=False)
tabela.rename(columns={"NUM_BO": "FrequenciaAbs"}, inplace=True)
tabela["FrequenciaAbsAcumulada"] = tabela["FrequenciaAbs"].cumsum()
tabela["FrequenciaRelativa"] = tabela["FrequenciaAbs"]/tabela["FrequenciaAbs"].sum()
tabela["FrequemcoaRelativaAcumulada"] = tabela["FrequenciaRelativa"].cumsum()

tabela
# %%
tabela = df.groupby("HORA_FATO")[["NUM_BO"]].count().sort_values("NUM_BO", ascending=False).head(10)
sns.barplot(tabela, y="HORA_FATO", x="NUM_BO")
plt.xlabel("Frequência")
plt.ylabel("Hora")
plt.title("Os 10 horários mais comuns que aconteceram feminicídio entre 2015 ~ 2022")
# %%
tabela
# %%
