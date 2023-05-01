# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior = 0
menor = 0
print(f'Os valores sorteados foram:', end=' ')
for c in range(0, len(tupla)):
    print(tupla[c], end=' ')

    if c == 0:
        maior = tupla[c]
        menor = tupla[c]
    elif tupla[c] > maior:
        maior = tupla[c]
    elif tupla[c] < menor:
        menor = tupla[c]

print(f'\nO maior valor sorteado foi: {maior}\nE o menor valor foi: {menor}')
