# %%

nomes = ["Maria", "Joana", "Lorena", "Natasha", "Jô", "Verônica"]

for nome in nomes: 
    if len(nome) <= 4:
        print(nome, "é um nome curto.")
    else:
        print(nome, "é um nome longo.")     