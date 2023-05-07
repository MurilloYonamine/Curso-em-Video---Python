# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = [[], [], []]
soma = somaColuna = maiorLinha = 0
for c in range(0, 3):
    for d in range(0, 3):

        # Pergunta ao usuário
        n = int(input(f'Digite um valor para [{c}, {d}]: '))

        # Verificação se o número é par
        if n % 2 == 0:
            soma = soma + n

        # Adição do número à lista
        lista[c].append(n)

        # Condições para descobrir o maior valor da segunda linha
        if c == 1:
            if maiorLinha == 0:
                maiorLinha = n
                menor = n
            elif n > maiorLinha:
                maiorLinha = n


for c in range(0, len(lista)):
    print()
    for d in range(0, len(lista)):
        print(f'[{lista[c][d]:^5}]', end='')

        if d == 2:
            somaColuna = somaColuna + lista[c][d]
print()
print(f'A soma dos valores é: {soma}.')
print(f'A soma dos valores da terceira coluna é {somaColuna}.')
print(f'O maior valor da segunda coluna é {maiorLinha}.')
