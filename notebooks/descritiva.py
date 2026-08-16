import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
ax.set_title("Difença entre número de casos entre SSP e IPEA no Estado de SP")
ax.set_ylabel("diferença")
ax.set_xticks(range(2011,2024, 2))
plt.show()
