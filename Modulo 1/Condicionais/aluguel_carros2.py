carro = input('Qual foi o modelo do carro alugado? ')
dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos km o carro rodou: '))
diaria = 0
if carro == 'Mitsubishi Eclipse':
    diaria = 200
elif carro == 'Nissan Skyline GT-R R34':
    diaria = 350
elif carro == 'Toyota Supra':
    diaria = 300
else:
    diaria = 70
valor_dias = (dias*diaria)
total_km = (km*0.15)
soma = valor_dias+total_km
print(f'Você andou {dias} por {km} dias, então o preço a pagar é R$ {soma:.2f}')