# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
dado = []
lista = []
pessoaMaiorPeso = []
pessoaMenorPeso = []
maiorPeso = 0
menorPeso = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    lista.append(dado[:])
    dado.clear()

    escolha = input('Deseja Continuar? [S/N]: ').upper()
    if escolha not in 'SN':
        escolha = input('Tente novamente. Deseja Continuar? [S/N]: ').upper()
    if escolha == 'N':
        break

for d in range(0, len(lista)):
    if maiorPeso == 0 and menorPeso == 0:
        maiorPeso = lista[d][1]
        menorPeso = lista[d][1]

    if lista[d][1] >= maiorPeso:
        if lista[d][1] == maiorPeso:
            maiorPeso = lista[d][1]
            pessoaMaiorPeso.append(lista[d][0])
        else:
            maiorPeso = lista[d][1]
            pessoaMaiorPeso.clear()
            pessoaMaiorPeso.append(lista[d][0])

    elif lista[d][1] <= menorPeso:
        if lista[d][1] == menorPeso:
            menorPeso = lista[d][1]
            pessoaMenorPeso.append(lista[d][0])
        else:
            menorPeso = lista[d][1]
            pessoaMenorPeso.clear()
            pessoaMenorPeso.append(lista[d][0])

print(lista)
print(f"Ao todo, foram cadastrados: {len(lista)} pessoas.")
print(f"O maior peso foi de {maiorPeso}. Peso de {pessoaMaiorPeso}.")
print(f"O menor peso foi de {menorPeso}. Peso de {pessoaMenorPeso}.")
