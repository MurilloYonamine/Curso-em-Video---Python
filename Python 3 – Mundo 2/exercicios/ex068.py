# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

print('=-' * 8, '\nPAR OU ÍMPAR')

while True:
    print('=-' * 8)
    player = int(input('Digite um valor: '))
    npc = random.randint(0, 10)

    escolha = input('Par ou ímpar? [P/I]: ').upper()
    print('---' * 10)

    soma = player + npc
    resultado = ""
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"

    print(f'Você jogou {player} e o computador {npc}. No total deu: {soma}. LOGO {resultado}!')

    print('---' * 10)
    if escolha == resultado[0]:
        print('Você venceu!!!')
        print('Vamos jogar novamente...')
    else:
        print('Você perdeu!!!')
        break
