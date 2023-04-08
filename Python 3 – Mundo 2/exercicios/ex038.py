# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print(f'{n1} é o maior valor!')
elif n2 > n1:
    print(f'{n2} é o maior valor!')
else:
    print(f'{n1} é igual a {n2}!')
