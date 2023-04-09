# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

aux = 0
pesoMaior = 0
pesoMenor = 0
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}º pessoa: '))

    if i == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso

print(f'O maior peso foi: {pesoMaior} Kg')
print(f'O menor peso foi: {pesoMenor} Kg')
