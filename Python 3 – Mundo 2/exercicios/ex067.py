# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Qual tabuada você deseja ver? '))
    print("---" * 12)

    if n < 0:
        print("PROGRAMA DA TABUADA ENCERRADO!")
        break

    print(f'{n} x 1 = {n * 1}'
          f'\n{n} x 2 = {n * 2}'
          f'\n{n} x 3 = {n * 3}'
          f'\n{n} x 4 = {n * 4}'
          f'\n{n} x 5 = {n * 5}'
          f'\n{n} x 6 = {n * 6}'
          f'\n{n} x 7 = {n * 7}'
          f'\n{n} x 8 = {n * 8}'
          f'\n{n} x 9 = {n * 9}'
          f'\n{n} x 10 = {n * 10}')
    print("---" * 12)
