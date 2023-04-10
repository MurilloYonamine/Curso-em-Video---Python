# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

escolha = 0

# Pergunta dos valores
n = float(input('Digite um valor: '))
n1 = float(input('Digite mais um valor: '))

# Laço do menu
while escolha != 5:

    # Menu de opções
    escolha = int(input("""
O que você deseja fazer?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Escolha: """))

    # Laço para caso o usuário seja curioso
    while not 0 < escolha < 6:
        escolha = int(input('Digite um valor entre 1-5! '))

    # Soma
    if escolha == 1:
        soma = n + n1
        print(f'A soma entre {n:.0f} e {n1:.0f} é: {soma:.0f}!')

    # Multiplicação
    if escolha == 2:
        multiplicacao = n * n1
        print(f'A soma entre {n:.0f} e {n1:.0f} é: {multiplicacao:.0f}!')

    # Maior número
    if escolha == 3:
        if n > n1:
            print(f'O maior número entre {n:.0f} e {n1:.0f} é: {n:.0f}')
        else:
            print(f'O maior número entre {n:.0f} e {n1:.0f} é: {n1:.0f}')

    # Novos números
    if escolha == 4:
        n = float(input('Digite um novo valor: '))
        n1 = float(input('Digite mais um novo valor: '))

    if escolha == 5:
        print('Finalizando...')
        sleep(0.5)
print('Fim do programa!')

