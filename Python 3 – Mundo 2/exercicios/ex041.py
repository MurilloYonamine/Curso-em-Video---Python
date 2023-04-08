# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER
from datetime import date
from time import time, sleep

anoAtual = date.today().year
ano = int(input('Que ano você nasceu? '))
idade = anoAtual - ano

if idade >= anoAtual:
    print('Coloque uma idade certa!')
elif idade <= 9:
    print(f'Com {idade} anos.')
    sleep(2)
    print(f'Você é um atleta MIRIM!')

elif 9 < idade <= 14:
    print(f'Com {idade} anos.')
    sleep(2)
    print(f'Você é um atleta INFANTIL!')

elif 14 < idade <= 19:
    print(f'Com {idade} anos.')
    sleep(2)
    print(f'Você é um atleta JÚNIOR!')

elif 19 < idade <= 25:
    print(f'Com {idade} anos.')
    sleep(2)
    print(f'Você é um atleta SÊNIOR!')
else:
    print(f'Com {idade} anos.')
    sleep(2)
    print(f'Você é um atleta SÊNIOR!')
