# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dado = dict()
dado['nome'] = input('Nome: ')
dado['media'] = float(input(f'Média de {dado["nome"]}: '))

print('---' * 15)

print(f'- Nome é igual a {dado["nome"]}')
print(f'- Média é igual a {dado["media"]}')

if dado['media'] >= 7:
    dado['situacao'] = 'Aprovado'
elif 5 <= dado['media'] <= 7:
    dado['situacao'] = 'Recuperação'
else:
    dado['situacao'] = 'Reprovado'
print(f'- Situação é igual a {dado["situacao"]}')
