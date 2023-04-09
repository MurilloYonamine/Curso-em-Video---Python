# Faça um programa que calcule a soma entre todos os números que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.

soma = 0
qtd = 0
for c in range(0, 501):
    if c % 3 == 0 and c % 2 != 0:
        qtd += +1
        soma += + c
print(f'A soma de todos os {qtd} valores é igual a: {soma}!')
