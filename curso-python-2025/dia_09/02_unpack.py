# %%

A = 1 
B = 5

print(A)
print(B)
# %%

C = A 
A = B
B = C
print(A)
print(B)
# %%

A, B = B, A
print(A)
print(B)
# %%
#c, d = A, B # c recebe valor de A e d recebe valor de B.

B, A = A, B
# %%

a, b,*resto = 1,2, 3,4, 5655, 2.1 # *args
print(a,b,resto)

# %%
a,*resto,b = 1,2, 3,4, 5655, 2.1 # pegar 1 e último.
print(a,b,resto)

# %%
*resto, a, b = 1,2, 3,4, 5655, 2.1
print(a,b,resto)
# %%

dados = {"nome": "teo", "sobrenome": "calvo"}
for i, j in dados.items():
    print(i,j)