# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = [int(), int(), int(), int(), int()]
maior = 0
menor = 0
posicaoMaior = []
posicaoMenor = []

for c in range(0, 5):
    lista[c] = int(input(f'Digite um número para a posição {c}º: '))

    if c == 0:
        maior = menor = lista[c]
    if menor >= lista[c]:
        menor = lista[c]
        posicaoMenor.append(c)
    elif lista[c] >= maior:
        maior = lista[c]
        posicaoMaior.append(c)

print(f'Você digitou os números: {lista}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
