# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time

n = random.randint(0, 5)

p1 = int(input('Digite um número entre 0 e 5: '))

if p1 > 5:
    print('Esse número está além do intervalo de 0 e 5.')
elif p1 == n:
    print(f'Você escolheu: {p1}.')
    print('Loading...')

    print(f'O bot escolheu: {time.sleep(2)} {n}.')
    print('Você adivinhou o número!')
else:
    print(f'Você escolheu: {p1}.')
    print('Loading...')
    time.sleep(2)
    print(f'O bot escolheu: {n}.')
    print('Você não adivinhou o número!')
