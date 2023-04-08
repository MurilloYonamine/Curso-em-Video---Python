# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO
import time

n1 = float(input('Qual é a primeira nota? '))
n2 = float(input('Qual é a segunda nota? '))
media = (n1 + n2) / 2

if 5 <= media <= 6.9:
    print(f'\nCom as notas: {n1} e {n2}...')
    time.sleep(2)
    print(f'Você tem uma média de: {media}!'
          f'\nPortanto, PARA RECUPERAÇÃO!')

elif media >= 7:
    print(f'\nCom as notas: {n1} e {n2}...')
    time.sleep(2)
    print(f'Você tem uma média de: {media}!'
          f'\nPortanto, APROVADO!')

else:
    print(f'\nCom as notas: {n1} e {n2}...')
    time.sleep(2)
    print(f'Você tem uma média de: {media}!'
          f'\nPortanto, REPROVADO!')
