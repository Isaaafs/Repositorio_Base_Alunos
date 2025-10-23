# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE
qntd_filmes = int(input('Quantos filmes deseja adicionar: '))
cont = 0
while cont<qntd_filmes:
    filme_novo = input('Digite o nome do filme: ')
    filmes.append(filme_novo)
    cont+=1


# LOOP FOR
qtd_filmes = int(input('Quantos filmes deseja adicionar: '))
for i in range (qtd_filmes):
    novo_filme = input('Digite o nome do filme: ')
    filmes.append(novo_filme)
print(filmes)
