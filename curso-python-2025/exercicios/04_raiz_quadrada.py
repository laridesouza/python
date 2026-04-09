numero = input("Entre com um número inteiro para calcular a sua raíz quadrada: ")

numero = int(numero)

raiz = numero ** (1/2) # numero ** 0.5
raiz = round(raiz, 4)
print("Raíz quadrada de", numero, "é:", raiz)