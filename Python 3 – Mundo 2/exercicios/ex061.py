#  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.

n = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a sua razao? '))
c = 0
pa = 0
while c != 10:
    c = c + 1
    pa = n + (c - 1) * razao
    print(pa, end=" -> ")
print('FIM')
