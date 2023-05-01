# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('eu', 'amo', 'o', 'Sales', 'Bowen', 'Berloffa')

for c in range(0, len(tupla)):
    print(f'\nNa palavra {tupla[c]} temos:', end=' ')

    if "a" in tupla[c]:
        print("a", end=' ')
    if "e" in tupla[c]:
        print("e", end=' ')
    if "i" in tupla[c]:
        print("i", end=' ')
    if "o" in tupla[c]:
        print("o", end=' ')
    if "u" in tupla[c]:
        print("u", end=' ')
