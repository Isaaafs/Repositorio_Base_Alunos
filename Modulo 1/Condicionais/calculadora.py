print(f'|{"-"*30}|')
print('| Calculadora')
print(f'|{"-"*30}|')
print('| 1 - Soma')
print('| 2 - Subtração')
print('| 3 - Multiplicação')
print('| 4 - Divisão')
print(f'|{"-"*30}|')
operador = int(input('Escolha uma das opções: '))
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
if operador == 1:
    print(f'O resultado é: {numero1+numero2}')
elif operador == 2:
    print(f'O resultado é: {numero1-numero2}')
elif operador == 3:
    print(f'O resultado é: {numero1*numero2}')
elif operador == 4:
    print(f'O resultado é: {numero1/numero2}')
else:
    print('Erro Digite algo valido')