# escreva um programa que solicite ao usuário frases. 
# para parar de solicitar frases, ele pode apertar apenas o "enter".
# seu programa deve apresentar cada frase e quantas vezes ela foi repetida.

dados = {}

while True:
    frase = input("Entre com a frase: ")
    if frase == "":
        break
    
    if frase not in dados: 
        dados[frase] = 1
    else: 
        dados[frase] += 1     
    
for i, j in dados.items():
    print(i, "->", j)

# %%
dados = {
    "oi": 1,
    "ola": 10,
    "oi tudo bem": 3,
    "test": 2,
    "teste": 5,
}

items = list(dados.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    print(i, "->", j)


