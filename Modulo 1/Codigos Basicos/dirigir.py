quantos_anos = int(input('Quantos anos você tem? '))
habilitacao = input('Você possui habilitação? (s/n)')
print(f'Pode dirigir? {quantos_anos>=18 and habilitacao=='s'}')