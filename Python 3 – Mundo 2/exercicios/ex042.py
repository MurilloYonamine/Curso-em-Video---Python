# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

n1 = float(input('Qual é o valor do primeiro lado? '))
n2 = float(input('Qual é o valor do segundo lado? '))
n3 = float(input('Qual é o valor do terceiro lado? '))

if n1 + n2 <= n3 or n1 + n3 <= n2 or n2 + n3 <= n1:
    print(f'Um triângulo, com as medidas: {n1}, {n2} e {n3}.\nNão pode ser formado!')
elif n1 == n2 == n3:
    print(f'Com os valores: {n1}, {n2} e {n3}.'
          f'\nVocê tem um triângulo EQUILÁTERO!')

elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
    print(f'Com os valores: {n1}, {n2} e {n3}.'
          f'\nVocê tem um triângulo ISÓSCELES!')

else:
    print(f'Com os valores: {n1}, {n2} e {n3}.'
          f'\nVocê tem um triângulo ESCALENO!')
