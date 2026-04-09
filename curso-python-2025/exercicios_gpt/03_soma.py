
# Crie uma função soma_dois_numeros(a, b) que recebe dois números e retorna a soma entre eles.
# Teste com diferentes valores.


def soma_dois_numeros(a:float,b:float)->float:
    valores = [a, b]
    return sum(valores)

a = float(input("Insira um número: "))
b = float(input("Insira outro número: "))
print("A soma dos valores é: ", soma_dois_numeros(a,b))

