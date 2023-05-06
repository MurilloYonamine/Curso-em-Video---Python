# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
lista = [[], [], []]
for c in range(0, 3):
    for d in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {d}]: '))
        lista[c].append(n)

for c in range(0, len(lista)):
    print()
    for d in range(0, len(lista)):
        print(f'[{lista[c][d]:^5}]', end='')
