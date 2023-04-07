# Escreva um programa que pergunte o salário de um funcionário
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário? '))

if salario >= 1251:
    aumento = salario + (salario * 10 / 100)
    print(f'Com um aumento de 10%, o salário atual será: R$ {aumento:.2f}!')
else:
    aumento = salario + (salario * 15 / 100)
    print(f'Com um aumento de 15%, o salário atual será: R$ {aumento:.2f}!')
