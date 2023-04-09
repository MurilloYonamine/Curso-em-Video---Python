# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

n = input('Digite um palíndromo: ').upper().strip()
n2 = n.split()
junto = ''.join(n2)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso)

if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')