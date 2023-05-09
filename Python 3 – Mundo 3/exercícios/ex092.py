# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS diferir de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

dado = {
    'nome': input('Nome: '),
    'idade': date.today().year - int(input('Ano de nascimento: ')),
    'cpts': input('Carteira de trabalho (0 não tem): ')
}

if dado['cpts'] != '0':
    dado['contratação'] = int(input('Ano de contratação: '))
    dado['salario'] = int(input('Salário: R$ '))
    dado['aposentadoria'] = dado['idade'] + ((dado['contratação'] + 35) - date.today().year)

    for c, d in dado.items():
        print(f'- {c} tem o valor {d}')
else:
    for c, d in dado.items():
        print(f'- {c} tem o valor {d}')
