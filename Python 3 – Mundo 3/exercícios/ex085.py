# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]

for c in range(0, 7):
    dado = int(input(f'Digite o {c}º número: '))

    if dado % 2 == 0:
        lista[0].append(dado)
    else:
        lista[1].append(dado)

lista[0].sort()
lista[1].sort()
print(f'Números pares: {lista[0]}')
print(f'Números ímpares: {lista[1]}')
