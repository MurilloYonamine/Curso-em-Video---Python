# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = dict()
lista = []
mulheres = []
idadeAcima = []
media = soma = 0
while True:
    dados.clear()

    dados['nome'] = input('Nome: ')
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()

    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Erro! Por favor digite M ou F: ')).upper()

    dados['idade'] = int(input('Idade: '))
    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    lista.append(dados.copy())

    if escolha not in 'SN':
        escolha = str(input('Erro! Por favor digite S ou N: '))

    if escolha == 'N':
        break

print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')

for c in range(0, len(lista)):
    soma = soma + lista[c]['idade']
    media = soma / len(lista)

    if lista[c]['sexo'] == 'F':
        mulheres.append(lista[c]['nome'])

print(f'B) A média de idade é: {media:.0f}')

print(f'C) As mulheres cadastradas foram:', end=' ')
for c in range(0, len(mulheres)):
    print(mulheres[c], end=' ')

print()
print(f'D) Lista de pessoas que estão acima da média:')
for c in range(0, len(lista)):
    if lista[c]['idade'] > media:
        idadeAcima.append(lista[c])

for c in range(0, len(idadeAcima)):
    print(f'    Nome = {idadeAcima[c]["nome"]}; Sexo = {idadeAcima[c]["sexo"]}; Idade = {idadeAcima[c]["idade"]}')

