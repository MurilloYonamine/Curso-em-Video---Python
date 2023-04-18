# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, o qual a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = int(input('Digite um número: [999 para parar]: '))
soma = 0
qtd = 0
while n != 999:
    soma = soma + n
    qtd = qtd + 1
    n = int(input('Digite um número: [999 para parar]: '))

print(f'Você digitou {qtd} números e a soma entre eles foi {soma}.')