# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? '))
desconto = preco - preco * (5 / 100)

print(f'O preço de R$ {preco:.2f} do produto com 5% é: R$ {desconto:.2f}')
