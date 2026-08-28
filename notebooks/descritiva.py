# %%
import pandas as pd

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
