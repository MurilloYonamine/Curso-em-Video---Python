# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

times = (
    'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico Paranaense',
    'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América Mineiro', 'Botafogo', 'Santos', 'Goiás',
    'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético Goieniense', 'Avaí', 'Juventude')

print('Os cinco primeiros times foram:')
for c in range(0, 5):
    print(f'{c + 1}º {times[c]}')
print()

print(f'Os quatro últimos foram: ')
for c in range(0, 4):
    print(f'{(len(times) - 3) + c}º {times[-4 + c]}')
print()

print(f'Todos os times em ordem alfabética: {sorted(times)}')

for c in range(0, len(times)):
    if times[c] == 'Cuiabá':
        print(f'\nO cuiabá está na {c+1}º posição')