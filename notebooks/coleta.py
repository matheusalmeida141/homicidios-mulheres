
#%%


import pandas as pd
import requests


for i in range(2011, 2026):
    response = requests.get(f"https://www.ssp.sp.gov.br/v1/ViolenciaMulher/RecuperaDadosPorAno?ano={i}")

    if response.status_code == 200:
        print("Requisição 🟢")

        df = pd.DataFrame()

        lst = []
        for k in response.json()['data'][0]['dadosMes']:
            lst.append(k['delito'])

        del k

        dfDelitos = pd.DataFrame(lst)
        dfDelitos = dfDelitos.drop(columns=['idGrupoDelito', 'ordem'])
        dfDelitos = dfDelitos.set_index('idDelito')




        for j in range(len(response.json()['data'])):

            mes = response.json()['data'][j]['mes']
            dfaux = pd.DataFrame(response.json()['data'][j]['dadosMes'])
            dfaux = dfaux.drop(columns="delito")
            dfaux['mes'] = mes

            df = pd.concat([df, dfaux])
            
       

        df = df.join(dfDelitos, on="idDelito", how="left")

        del dfDelitos
        del dfaux  
        df["ano"] = i

        df.to_csv(f"../data/violencia-mulher-{i}.csv", index=False, encoding="utf-8")
        
        del df
        
        print("CSV gerado com sucesso!")
    else:
        print("Requisição 🔴")


# %%

