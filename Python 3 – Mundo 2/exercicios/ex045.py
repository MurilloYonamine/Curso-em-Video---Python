# Crie um programa que faça o computador jogar Jokenpô com você.
import random
import time

print('SEJA BEM VINDO A DISPUTA DE JOKENPÔ!')
escolha = int(input("""QUAL SERÁ A SUA ESCOLHA?
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Qual será sua jogada? """))

if escolha > 3 or escolha < 1:
    print('Escolha um número dentro do intervalo de 1-3!')
    exit()

oponente = random.randint(1, 3)

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
time.sleep(0.5)

if escolha == 1:
    print('-=' * 20)
    print('Você escolheu PEDRA! \U0001f44a')

    if oponente == 1:
        print('O seu oponente escolheu PEDRA! \U0001f44a')
        print('-=' * 25)
        time.sleep(1)
        print('PEDRA com PEDRA é EMPATE!')
    elif oponente == 2:
        print(f'O seu oponente escolheu PAPEL! \U0001f590\ufe0f')
        print('-=' * 25)
        time.sleep(1)
        print('PAPEL com PEDRA é VITÓRIA DO OPONENTE!!')
    else:
        print('O seu oponente escolheu TESOURA! \u270c\ufe0f')
        print('-=' * 25)
        time.sleep(1)
        print('TESOURA com PEDRA é VITÓRIA DO JOGADOR!!')

if escolha == 2:
    print('-=' * 20)
    print('Você escolheu PAPEL! \U0001f590\ufe0f')

    if oponente == 1:
        print('O seu oponente escolheu PEDRA! \U0001f44a')
        print('-=' * 25)
        time.sleep(1)
        print('PEDRA com PAPEL é VITÓRIA DO JOGADOR!')
    elif oponente == 2:
        print('O seu oponente escolheu PAPEL! \U0001f590\ufe0f')
        print('-=' * 25)
        time.sleep(1)
        print('PAPEL com PAPEL é EMPATE!!')
    else:
        print('O seu oponente escolheu TESOURA! \u270c\ufe0f')
        print('-=' * 25)
        time.sleep(1)
        print('TESOURA com PAPEL é VITÓRIA DO OPONENTE!!')

if escolha == 3:
    print('-=' * 20)
    print('Você escolheu TESOURA! \u270c\ufe0f')

    if oponente == 1:
        print('O seu oponente escolheu PEDRA! \U0001f44a')
        print('-=' * 25)
        time.sleep(1)
        print('PEDRA com TESOURA é VITÓRIA DO OPONENTE!')
    elif oponente == 2:
        print('O seu oponente escolheu PAPEL! \U0001f590\ufe0f')
        print('-=' * 25)
        time.sleep(1)
        print('PAPEL com TESOURA é VITÓRIA DO JOGADOR!!')
    else:
        print('O seu oponente escolheu TESOURA! \u270c\ufe0f')
        print('-=' * 25)
        time.sleep(1)
        print('TESOURA com TESOURA é EMPATE!!')
