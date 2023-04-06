# Faça um algoritmo que leia o salário de um funcionário e mostre sue novos salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? '))
aumento = salario + salario*(15/100)

print(f'O salário de R$ {salario:.2f}, com 15% de aumento é: R$ {aumento:.2f}')