# Crie uma função media_simples(a, b, c) que recebe três números e retorna a média aritmética.

def media_simples(a:float, b:float, c:float):
    valores = [a, b, c]
    return sum(valores) / len(valores)

a = float(input("Insira um valor: "))
b = float(input("Insira um segundo valor: "))
c = float(input("Insira um terceiro valor: "))

print("A média aritmética dos números é: ", media_simples(a, b, c))