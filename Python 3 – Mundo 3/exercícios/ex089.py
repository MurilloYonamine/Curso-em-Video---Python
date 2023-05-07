# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.
dado = []
lista = []
while True:
    # Pergunta e adição dos elementos na lista
    dado.append(input('Nome: '))
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))
    lista.append(dado[:])
    dado.clear()

    # Pergunta ao usuário caso ele queira continuar adicionando dados
    escolha = input('Quer continuar? [S/N]: ').upper()
    while escolha not in 'SN':
        escolha = input('Tente novamente. Quer continuar? [S/N]: ').upper()
    if escolha == 'N':
        break

# Elementos para deixar a visualização mais bonita
print()
print(f'{"Num."} {"NOME":^10} {"Média":^10}')
print('-' * 24)

# Mostrar uma tabela de informações para o usuário
for c in range(0, len(lista)):
    media = soma = 0
    for d in range(1, 3):
        soma = soma + lista[c][d]
        media = soma / 2
    print(f'{c:^2} {lista[c][0]:^16} {media:.1f}')

# Vai puxar um dado dentro da tabela através de um número escolhido pelo usuário
while True:
    print()
    n = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))

    if n == 999:
        break

    while n >= len(lista):
        n = int(input('Digite um número válido! Mostrar notas de qual aluno? (999 Interrompe): '))
    else:
        print(f'As notas de {lista[n][0]} são: [{lista[n][1]:.1f}, {lista[n][2]:.1f}]')
