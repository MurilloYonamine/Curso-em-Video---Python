# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('Eu', 'amo', 'o', 'Sales', 'Bowen', 'Berloffa')

for c in range(0, len(tupla)):
    print(f'\nNa palavra {tupla[c]} temos:', end=' ')

    if tupla[c] in 'AEIOU':
        print(tupla[c].split())
