print('SISTEMA DE PROVAS')
total_provas = float(input('Quantas provas o aluno realizou: '))

contador = 1
soma = 0

while contador <= total_provas:
    valor_provas = float(input(f'Digite a nota da prova {contador}: '))
    contador += 1
    soma += valor_provas

media = soma/total_provas
print(f'O aluno obteve media {media:.2f}')