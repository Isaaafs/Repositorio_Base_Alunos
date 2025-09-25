# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',30*'-','|')
print('| SISTEMAS DE PROVAS')
print('|',30*'-','|')
nome = input('| Nome do aluno: ')
prova_1 = float(input('| Nota da primeira prova:'))
prova_2 = float(input('| Nota da segunda prova:'))
prova_3 = float(input('| Nota da terceira prova:'))
media = (prova_1+prova_2+prova_3)/3
print('|',30*'-','|')
print(f'| Aluno: {nome}')
print(f'| Media: {media:.2f}')
if media >=5:
    print('| Aluno aprovado')
else:
    print('| Aluno reprovado')
print('|',30*'-','|')