senha_correta = '030508'
tentativa = input('Tente adivanhar minha senha: ')

while tentativa != senha_correta:
    print('Você errou!')
    tentativa = input('Tente adivinhar minha senha: ')
print('Você acertou!')