# %%
for i in range(5):
    print(i)

# %% 
list(range(5,10))
# %%
list(range(0,100,10))
# %%
list(range(0,110,10))
# %%
list(range(-10,-110,-10))
# %%
a = ["Larissa", "de", "Souza", "Silva"] # criei uma lista
for i in range(len(a)): # len pega o tamanho da lista, range cria uma seq. de números com os índices da lista e for i in range vai fazer o código rodar len(a) vezes.
    print(i, a[i]) # i mostra o número do índice e a[i], mostra o elemento da lista que corresponde ao índice.