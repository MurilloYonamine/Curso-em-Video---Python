# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

tupla = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))

print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu pela primeira vez na posição {tupla.index(3)+1}')
else:
    print('Não há 3 na tupla!')

print('Os valores pares digitados foram: ', end='')
for c in range(0, len(tupla)):
    print(tupla[c] if tupla[c] % 2 == 0 else '', end=' ')
