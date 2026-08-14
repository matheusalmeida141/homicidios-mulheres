
import pandas as pd
import requests

for i in range(2011, 2026):
    response = requests.get(f"https://www.ssp.sp.gov.br/v1/ViolenciaMulher/RecuperaDadosPorAno?ano={i}")

    if response.status_code == 200:
        print("Requisição 🟢")

        for j in range(0, 13):

            df = pd.DataFrame(response.json()['data'][j]['dadosMes'])
            df["mes"] = j

            df = df.drop(columns=['delito'])

        lst = []
        for j in response.json()['data'][1]['dadosMes']:
            lst.append(j['delito']) 
        df2 = pd.DataFrame(lst)
        df2.set_index("idDelito", inplace=True)
        df = df.join(df2, on=["idDelito"], how="left")
        df.drop(columns = ["idGrupoDelito", "ordem"], inplace= True)


        del df2

        #df.to_csv(f"../data/violencia-mulher-{i}.csv", index=True, encoding="utf-8")

        del df
        print("CSV gerado com sucesso!")
    else:
        print("Requisição 🔴")

