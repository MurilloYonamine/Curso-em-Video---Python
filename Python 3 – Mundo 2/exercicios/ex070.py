# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

total = 0
qtdMil = 0
barato = 0
baratoNome = ''

while True:
    print('---' * 10)
    print('       LOJÃO DO SALEZÃO')
    print('---' * 10)

    produto = input('Nome do produto? ')
    preco = float(input('Preço: R$ '))
    escolha = input('Deseja continuar? [S/N]? ').upper()

    total = total + preco

    # Quantidade de produtos custando mais de R$ 1000
    if preco > 1000:
        qtdMil = qtdMil + 1

    # Produto mais barato
    if barato == 0:
        barato = preco

    if barato > preco:
        barato = preco
        baratoNome = produto
    # Escolha do usuário
    while escolha not in 'SN':
        escolha = input('Apenas [S/N]!').upper()
    if escolha == 'N':
        break

print('-' * 10 + 'FIM DO PROGRAMA' + '-' * 10)
print(f'O total de compras foi; R${total:.2f}!')
print(f'Temos {qtdMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {baratoNome} que custa R${barato:.2f}!')