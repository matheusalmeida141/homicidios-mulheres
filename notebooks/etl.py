# %%
import pandas as pd

df = pd.DataFrame()
for i in range(2011, 2026):
    df2 = pd.read_csv(f"../data/violencia-mulher-{i}.csv",)
    df2["ano"] = i

    df = pd.concat([df, df2])
# %%
df[ df["idDelito"] == 134]
# %%
