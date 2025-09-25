from colorama import init,Fore
int(autoreset=True)
print(f'|{"_"*30}|')
print('| SISTEMAS DE PROVAS')
print(f'|{"_"*30}|')
nome = input('| Nome do aluno: ')
nota_1 = float(input('| Nota da primeira prova: '))
nota_2 = float(input('| Nota da segunda prova: '))
nota_3 = float(input('| Nota da terça prova: '))
media = (nota_1+nota_2+nota_3)/3
print(f'|{"_"*30}|')
print(f'| Aluno:{nome} | Aprovado? {media>=5}')