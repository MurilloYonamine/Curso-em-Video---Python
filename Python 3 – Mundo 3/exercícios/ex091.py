# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint

jogador = dict()
ranking = dict()

jogador['jogador1'] = randint(1, 6)
jogador['jogador2'] = randint(1, 6)
jogador['jogador3'] = randint(1, 6)
jogador['jogador4'] = randint(1, 6)

print('Valores sorteados: ')
for c, d in jogador.items():
    print(f'{c} tirou {d} no dado.')

print('---' * 15)
print('RANKING DOS JOGADORES')

for c in jogador.items():


c = 1
for d, e in jogador.items():
    print(f'{c}º lugar: {d} com {e}.')
    c = c +1
