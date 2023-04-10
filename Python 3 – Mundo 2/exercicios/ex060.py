# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Qual número fatorial você deseja saber? '))
n1 = n
fator = n

print(f'{n}! = ', end="")
while not n1 == 1:
    n1 = n1 - 1
    fator = fator * n1

    if n1 == 1:
        print(f'{n1} = ', end="")
    else:
        print(f'{n1} x ', end="")

print(f'{fator}.')
