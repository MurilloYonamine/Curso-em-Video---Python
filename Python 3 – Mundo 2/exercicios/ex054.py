# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

ano = date.today().year
maiorIdade = 0
menorIdade = 0

for c in range(1, 8):
    n = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = ano - n
    if idade < 18:
        print(f'A {c}º não atingiu a maioridade!')
        menorIdade += +1
    else:
        print(f'A {c}º atingiu a maioridade!')
        maiorIdade += +1
print(f'\nAo todos tivemos {maiorIdade} maiores de idade.'
      f'\nE também tivemos {menorIdade} menores de idade.')
