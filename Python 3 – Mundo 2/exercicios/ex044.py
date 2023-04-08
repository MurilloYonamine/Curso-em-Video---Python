# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

produto = float(input('Qual o valor que será pago pelo produto? R$ '))

forma = int(input("""Como será a forma de pagamento?
[ 1 } À vista dinheiro/cheque?
[ 2 } À vista no cartão?
[ 3 } 2x no cartão?
[ 4 } 3x no cartão?
Qual é a opção? """))

if forma == 1:
    print('Pagando à vista em dinheiro ou cheque, você tem direito a 10% de desconto!')
    desconto = produto - (produto * (10 / 100))
    print(f'O valor de R$ {produto:.2f} com 10% de desconto é: R$ {desconto:.2f}!')

elif forma == 2:
    print('Pagando à vista no cartão, você tem direito a 5% de desconto!')
    desconto = produto - (produto * (5 / 100))
    print(f'O valor de R$ {produto:.2f} com 5% de desconto é: R$ {desconto:.2f}!')

elif forma == 3:
    print('Parcelando 2x no cartão, você não tem direito a desconto.'
          f'\nPortanto há de ser pago: R$ {produto:.2f}!')

elif forma == 4:
    parcelas = int(input('Serão quantas parcelas? '))
    juros = (produto + (produto * (20 / 100))) / parcelas
    precoJuros = produto + (produto * (20 / 100))
    print(f'Sua compra, com {parcelas} parcelas, custará {parcelas}x de R$ {juros:.2f} COM JUROS!'
          f'\nSua compra de R$ {produto:.2f}, vai custar R$ {precoJuros:.2f} no final!')
