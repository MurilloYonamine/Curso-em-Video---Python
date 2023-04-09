# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Variáveis
idades = 0
mediaIdade = 0

idadeMaiorM = 0
idadeMenorM = 0
homemVelho = ''

idadeMaiorF = 0
idadeMenorF = 0
qtdM = 0

for c in range(1, 5):

    # Negócio para deixar bonito
    print('\n' + '=' * 30, end='')
    print(f'\n           {c}º PESSOA\n', end='')
    print('=' * 30)

    # perguntas
    nome = input(f'Qual o nome da {c}º pessoa? ')
    idade = int(input(f'Qual a idade da {c}º pessoa? '))
    sexo = input(f'Sexo da {c}º pessoa [M/F]: ').upper()

    # Média das idades
    idades += +idade
    mediaIdade = idades / c

    # Homem mais velho
    if c == 1 and sexo == 'M':
        idadeMaiorM = idade
        idadeMenorM = idade
    if idade > idadeMaiorM and sexo == 'M':
        idadeMaiorM = idade
        homemVelho = nome
    else:
        idadeMenorM = idade

    # Mulheres com idade menor que 20
    if idade < 20 and sexo == 'F':
        qtdM += +1

print(f'\nA média de idade do grupo é: {mediaIdade} anos.')
print(f'O homem mais velho tem {idadeMaiorM} anos e se chama {homemVelho}!')
print(f'Ao todo são {qtdM} mulheres com menos de 20 anos.')
