# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
from time import sleep

lista = []
while True:
    n = int(input('Digite um valor: '))
    sleep(0.5)
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado.')
    sleep(0.5)

    escolha = input('Quer continuar? [S/N]: ').upper()
    while escolha not in 'SN':
        escolha = input('Tente novamente. Quer continuar? [S/N]: ').upper()
    if escolha in 'Nn':
        break

lista.sort()

print(lista)
