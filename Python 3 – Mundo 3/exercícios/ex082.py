# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

listaPares = list()
listaImpares = list()
lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))

    escolha = str(input('Deseja Continuar? [S/N]: ')).upper()

    while escolha not in 'SN':
        escolha = str(input('Tente Novamente. Deseja Continuar? [S/N]')).upper()

    if escolha == 'N':
        break

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        listaPares.append(lista[c])
    else:
        listaImpares.append(lista[c])

print(f'A lista completa é: {lista}')
print(f'A lista apenas com pares é: {listaPares}')
print(f'A lista apenas com ímpares é: {listaImpares}')
