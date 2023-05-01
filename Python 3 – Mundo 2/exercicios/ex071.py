# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('---' * 10)
print('         BANCO SALES')
print('---' * 10)

valor = float(input('Qual valor você quer sacar? '))
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
while True:

    while valor >= 50:
        valor = valor - 50
        nota50 = nota50 + 1

        if valor < 50:
            print(f'Total de {nota50} cédulas de R$50')
            break

    while valor >= 20:
        valor = valor - 20
        nota20 = nota20 + 1

        if valor < 20:
            print(f'Total de {nota20} cédulas de R$20')
            break

    while valor >= 10:
        valor = valor - 10
        nota10 = nota10 + 1

        if valor < 10:
            print(f'Total de {nota10} cédulas de R$10')
            break

    while valor >= 1:
        valor = valor - 1
        nota1 = nota1 + 1

        if valor < 1:
            print(f'Total de {nota1} cédulas de R$1')
            break
    break

print('---' * 10)
print('Volte sempre ao banco sales! Tenha um bom dia.')
