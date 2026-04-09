# %%
nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file: # enquanto esse arquivo tiver aberto, processar o dado.
    conteudo = open_file.read()

# quando sair do escopo do with, o arquivo será fechado automaticamente. 
print(conteudo)    



# abre o arquivo em formato de leitura
open_file = open(nome_arquivo)
# %%

# lê os dados do arquivo
conteudo = open_file.read() # read é método.
print(conteudo)

# %%

# fecha arquivo
open_file.close()
