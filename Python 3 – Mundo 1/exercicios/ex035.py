# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = float(input('Digite o valor da primeira reta: '))
n2 = float(input('Digite o valor da segunda reta: '))
n3 = float(input('Digite o valor da terceira reta: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print(f'Um triângulo, com as medidas: {n1}, {n2} e {n3}. Pode ser formado!')
else:
    print(f'Um triângulo, com as medidas: {n1}, {n2} e {n3}. Não pode ser formado!')
