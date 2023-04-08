# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Salário do comprador: '))
financiamento = int(input('Quantos anos de financiamento? '))

if (casa / (financiamento * 12)) > salario * (30 / 100):
    print(
        f'Para pagar uma casa de R$ {casa:.2f} em {financiamento} anos, a prestação será de: R$ {casa / (financiamento * 12):.2f}!'
        f'\nEmpréstimo negado!')
else:
    print(
        f'Para pagar uma casa de R$ {casa:.2f} em {financiamento} anos, a prestação será de: R$ {casa / (financiamento * 12):.2f}!'
        f'\nEmpréstimo aceito!')
