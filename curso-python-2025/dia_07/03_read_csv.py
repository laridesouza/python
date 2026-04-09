# %%
arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)

# %%

dados = dict()

chaves = lines[0].strip("\n").split(";")
for c in chaves: # percorre as chaves (nome, idade, profissão).
    dados[c] = [] # atribui as chaves uma lista vazia.

dados
# %%

for l in lines[1:]: # percorre todas as linhas a partir da segunda linha.

    valores = l.strip("\n").split(";") # para primeira linha que foi pega(que é a segunda), é removido o \n e os valores são separados em uma lista a partir do ; . 

# para passar por todas as chaves do dicionário(que está vazio) e adicionar os valores garantindo a ordem.
    for i in range(0, len(valores)): # percorre o i (índice) que começa em 0 e vai até o número de valores obtidos (0, 2).

# para atribuir os valores recebidos ao dicionário.
        dados[chaves[i]].append(valores[i]) # garante que pega o mesmo índice da chave correspondente ao valor. ex: i = 0 -> chaves = nome; valores = Teo
        # .append adiciona elemento a lista.
# %% 

idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/len(idades)
media 