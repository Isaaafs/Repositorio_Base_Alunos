# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

lista = [
{
    'Nome' : 'isabella',
    'Idade' : '17',
    'Cidade' : 'São Paulo'
},
{
    'Nome' : 'Geovanna',
    'Idade' : '16',
    'Cidade' : 'Santa Catarina'
},
{
    'Nome' : 'Mayra',
    'Idade' : '19',
    'Cidade' : 'Acre'
}
]

for i in lista:
    print(i['Nome'])