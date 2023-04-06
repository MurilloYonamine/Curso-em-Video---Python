# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Adote US$ 1.00 = 3.27

real = float(input('Quantos R$ você tem? '))

dolar = real * 3.27

print(f'Com R$ {real:.2f}, é possível comprar: US$ {dolar:.2f}')
