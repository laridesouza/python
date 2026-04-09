# %%

lista = ["joia", "lugar", "tabuada"]

for palavra in lista:
    contagem = 0 # “Para essa nova palavra que eu vou verificar, ainda não contei nenhuma vogal, então começo com zero.”
    for letra in palavra:
        if letra in "aeiou": #Se essa letra for uma vogal, somo +1 no meu contador de vogais.”
            contagem += 1
            print("A palavra", palavra, "tem", contagem, "vogais.")