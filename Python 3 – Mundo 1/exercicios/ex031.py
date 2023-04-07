# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

n = int(input('Diga a distância, em km, da sua viagem: '))

if n < 200:
    preco = n * 0.5
    print(f'Uma viagem de {n} km. Terá que ser pago R$ {preco:.2f}.')
else:
    preco = n * 0.45
    print(f'Uma viagem de {n} km. Terá que ser pago R$ {preco:.2f}.')
