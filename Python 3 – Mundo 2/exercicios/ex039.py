#  Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

anoAtual = datetime.date.today().year
ano = int(input('Qua ano você nasceu? '))
idade = anoAtual - ano

if idade < 18:
    falta = 18 - idade
    alistamento = anoAtual + falta
    print(f'Com {idade} anos, você ainda não tem idade para se alistar! \nAinda faltam {falta} anos! \nSeu alistamento será em: {alistamento}!')
elif idade > 18:
    atraso = idade - 18
    alistamento = anoAtual - atraso
    print(f'Com {idade} anos, você já passou da idade para se alistar! \nJá passou {atraso} anos! \nSeu alistamento deveria ter sido em: {alistamento}!')
else:
    print(f'Com {idade} anos, você já pode se alistar!')
