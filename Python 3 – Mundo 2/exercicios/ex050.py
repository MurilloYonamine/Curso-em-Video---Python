# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

qtdNumeros = 0
soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    qtdNumeros += + 1

    if n % 2 == 0:
        soma += + n

print(f'A soma dos {qtdNumeros} números é igual a: {soma}!')
