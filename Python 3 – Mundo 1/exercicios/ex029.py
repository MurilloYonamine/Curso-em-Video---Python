# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

n1 = int(input('Qual é a velocidade autal do carro? '))

if n1 > 80:
    print('Você ultrapassou o limite de velocidade!')
    multa = (n1 - 80) * 7

    print(f'Você terá que pagar uma multa de: R$ {multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
