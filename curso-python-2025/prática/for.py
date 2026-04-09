# %%

nomes = ["Viola", "Lauren", "Carolana","Carol", "Bel"]
for nome in nomes:
    print("O nome",nome,"tem", len(nome), "letras")

# %%
# nomes com mais de 5 letras

for nome in nomes:
    if len(nome) > 5:
        print(nome)
