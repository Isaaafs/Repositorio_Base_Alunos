
print(f'|{"_"*50}|')
print('| SISTEMAS DE PROVAS')
print(f'|{"_"*50}|')
nome = input('| Nome do aluno: ')
nota_1 = float(input('| Nota da primeira prova: '))
nota_2 = float(input('| Nota da segunda prova: '))
nota_3 = float(input('| Nota da terça prova: '))
media = (nota_1+nota_2+nota_3)/3
print(f'|{"_"*50}|')
if media >=6:
    print(f'| Aluno: {nome} | Você foi aprovado!!')
elif media == 5:
    print(f'| Aluno: {nome} | Você passou!')
else:
    print(f'| Aluno: {nome} | \033[31mVocê foi reprovado\033[0m')
print(f'|{"_"*50}|')