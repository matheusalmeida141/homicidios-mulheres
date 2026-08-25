# # %%
# import pandas as pd


# def to_csv(name: str, df:pd.DataFrame ):

#     df.to_csv(f"../data/{name}.csv", index=False)


# for i in range(2022, 2026):
#     df = pd.read_excel(f"../data/SPDadosCriminais_{2022}.xlsx", sheet_name=1)
#     df2 = pd.read_excel(f"../data/SPDadosCriminais_{2022}.xlsx", sheet_name=2)
#     to_csv(f"DadosCriminais_{i}", pd.concat([df, df2], axis= 0))
# # %%

# import pandas as pd

# df = pd.read_csv("../data/DadosCriminais_2022.csv", low_memory=False)
# # %%

# df.columns
# # %%

# df["NATUREZA_APURADA"].unique()
# # %%


# df = df[ (df["NATUREZA_APURADA"] == "ESTUPRO")                | 
#     (df["NATUREZA_APURADA"] == "HOMICÍDIO DOLOSO")       |
#     (df["NATUREZA_APURADA"] == "LESÃO CORPORAL DOLOSA")  |
#     (df["NATUREZA_APURADA"] == "TENTATIVA DE HOMICIDIO") |
#     (df["NATUREZA_APURADA"] == "ESTUPRO DE VULNERÁVEL")  |
#     (df["NATUREZA_APURADA"] == "LESÃO CORPORAL SEGUIDA DE MORTE")
#     ]




# %%
import pandas as pd


# %%
evento = ["Feminicídio", 
             "Homicídio doloso", 
             "Lesão corporal seguida de morte",
             "Tentativa de feminicídio",
             "Tentativa de homicídio",
             "Estupro",
             "Estupro de vulnerável",

             ]

for i in range(2023, 2026):
    df = pd.read_excel(f"../data/BancoVDE {i}.xlsx")

    df = df[ df["uf"] == "SP"]

    df = df[ df["evento"].isin(evento) ]
    df = df.query("total_vitima != 0 and (feminino > 0 or nao_informado > 0)")
    df.to_csv(f"../data/gov-homicidios-{i}.csv", index=False)
    print(i)

# %%
dfs = []
for i in range(2015, 2027):
    df = pd.read_csv(f"../data/gov-homicidios-{i}.csv")    
    dfs.append(df)

# %%
df = pd.concat(dfs, axis=0)

del dfs
# %%

df["data_referencia"] = pd.to_datetime(df["data_referencia"]).dt.year

#%%

df = df[ (df["evento"] == "Homícidio doloso") | (df["evento"] == "Feminicídio")]


df = df.groupby("data_referencia")[["feminino"]].sum().reset_index()
#%%

df.rename(columns={"data_referencia":"ano", "feminino":"total"}, inplace = True)
df["origem"] = "gov"

df
#%%
df2 = pd.read_csv("../data/homicidios.csv",)

df = pd.concat([df2,df], axis = 0)

df.to_csv("../data/homicidios.csv", index=False)
# %%
