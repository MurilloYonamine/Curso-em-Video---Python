# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

print('---' * 15)
print('                  MEGA-SENA')
print('---' * 15)

lista = []
numeros = []
cont = 6
n = int(input('Quantos jogos você quer que seja sorteado? '))
print(f'SORTEANDO {n} JOGOS')

for c in range(0, n):
    for d in range(0, cont):
        numeros.append(randint(1, 60))

    if numeros not in lista:
        lista.append(numeros[:])
    else:
        cont = cont + 1
    numeros.clear()

    sleep(1)
    lista[c].sort()
    print(f'Jogo {c + 1}: {lista[c]}')

print('-' * 16 + ' Boa sorte! ' + '-' * 16)
