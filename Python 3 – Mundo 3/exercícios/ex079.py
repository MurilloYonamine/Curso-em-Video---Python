# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
from time import sleep

c = 0
maior = 0
menor = 0
aux = 0
lista = []
while True:
    n = int(input('Digite um valor: '))
    # sleep(0.5)
    lista.append(n)

    for d in range(c + 1, len(lista)):
        if lista[c] == lista[d]:
            del lista[d]

    print('Valor adicionado com sucesso...')
    # sleep(0.5)

    escolha = input('Quer continuar? [S/N]: ').upper()
    while escolha not in 'SN':
        escolha = input('Tente novamente. Quer continuar? [S/N]: ').upper()
    if escolha == 'N':
        break

lista.sort()

print(lista)
