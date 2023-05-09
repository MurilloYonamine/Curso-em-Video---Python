# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter

jogador = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}

ranking = dict()

print('Valores sorteados: ')
for c, d in jogador.items():
    print(f'{c} tirou {d} no dado.')

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print('---' * 15)
print('RANKING DOS JOGADORES')
for c, d in enumerate(ranking):
    print(f'{c+1}º lugar: {d[0]} tirou {d[1]} no dado.')
