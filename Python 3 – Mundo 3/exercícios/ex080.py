# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
aux = 0
for c in range(0, 5):
    n = int(input(f'Digite o {c + 1}º valor: '))
    lista.append(n)

    for d in range(0, c):
        if lista[d] > lista[c]:
            aux = lista[c]
            lista[c] = lista[d]
            lista[d] = aux

    if c == 0:
        print(f'Adicionado no final da lista...')
    else:
        print(f'Valor adicionado na posição {c}...')

print(lista)
