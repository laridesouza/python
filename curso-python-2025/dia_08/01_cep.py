# %%
import requests # para realizar requisições na web
import json # para tratar listas/dicionários para arquivos json.
from tqdm import tqdm

import pandas as pd 

ceps = [
    "01519000",
    "13329120", 
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863",  
    "19060100",
    "58038200",
]

url = "https://viacep.com.br/ws/{cep}/json"
dados = [] # lista onde os ceps serão armazenados

for i in tqdm(ceps): # navega em todos os ceps
    resposta = requests.get(url.format(cep=i)) # obtém resposta da requests
    if resposta.status_code == 200: # 200 = sucesso
        dados.append(resposta.json()) # se foi sucesso, pega a resposta e trasnforma em json e adiciona na lista de dados. 


print(dados)
# %%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

# %%
with open("ceps.json", "w", encoding="utf-8") as open_file: # abre um arquivo "ceps.json" em modo de escrita
    json.dump(dados, open_file, ensure_ascii=False, indent=2) # pega a biblioteca json, utiliza o método dump, passa os dados, o arquivo que foi aberto, usa o argumento ensure_ascii=False para ignorar a tabela ascii e o indent para indentar de forma bonita.

