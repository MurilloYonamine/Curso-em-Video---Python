# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;33m', end=' ')
        div += +1
    else:
        print(f'\033[1;31m', end=' ')
    print(c, end=' ')

if div > 1:
    print(f'\n\033[mO número {n} foi divísivel {div}.')
    print(f'Por isso ele não é primo!')
else:
    print(f'\n\033[mOO número {n} foi divísivel {div}.')
    print(f'Por isso ele é primo!')
