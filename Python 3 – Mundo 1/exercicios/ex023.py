# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Digite um número de 0 a 9999: '))

print(f'Analisando o número {n}: ')

mil = (n / 1000)
cen = ((n / 1000) - int(n / 1000)) * 10
dez = ((n / 100) - int(n / 100)) * 10
uni = ((n / 10) - int(n / 10))*10

print(f'Unidade: {uni:.0f}.\n'
      f'Dezena: {dez:.0f}.\n'
      f'Centena: {cen:.0f}.\n'
      f'Milhar: {mil:.0f}.\n')
