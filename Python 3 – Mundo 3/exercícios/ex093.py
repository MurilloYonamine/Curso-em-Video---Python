# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
gols = []
total = 0

dados['nome'] = input('Nome do jogador: ')
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for c in range(0, dados['partidas']):
    gols.append(int(input(f'Quantos gols ele marcou na partida {c + 1}? ')))
    total = total + gols[c]
dados['gols'] = gols[:]
dados['total'] = total[:]

print(f'\n{dados}\n')

for c, d in dados.items():
    print(f'O campo {c} tem o valor {d}')

print(f'\nO jogador {dados["nome"]} jogou {dados["partidas"]} partidas:')

for c, d in enumerate(dados['gols']):
    print(f'    => Na partida {c+1}, fez {d} gols.')
print(f'Foi um total de {dados["total"]} gols')
