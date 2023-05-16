# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados = dict()
lista = list()
gols = list()
while True:
    dados.clear()
    gols.clear()
    total = 0
    dados['nome'] = input('Nome do jogador: ')
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c in range(0, dados['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
        total = total + gols[c]

    dados['gols'] = gols.copy()
    dados['total'] = total
    lista.append(dados.copy())

    escolha = input('Deseja continuar? [S/N] ').upper()

    while escolha not in 'SN':
        escolha = input('Tente novamente.Deseja continuar? [S/N] ').upper()

    if escolha == 'N':
        break

print('---' * 15)
print('cod      nome              gols               total')

for c in range(0, len(lista)):
    print(c, '      ', lista[c]["nome"], '     ', lista[c]["gols"], '            ', lista[c]["total"])

while escolha != 999:
    print('---' * 15)
    escolha = int(input('Mostrar dados de qual jogador? [999 para parar] '))

    if escolha == 999:
        break

    print(f'LEVANTAMENTO DO JOGADOR {lista[escolha]["nome"].upper()}')
    for c in range(0, len(lista[escolha]['gols'])):
        print(f'No jogo {c+1} fez {lista[escolha]["gols"][c]}.')

print('VOLTE SEMPRE!')
