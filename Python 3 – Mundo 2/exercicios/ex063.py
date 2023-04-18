# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Quantos termos você quer mostrar? '))
limite = 0
n1 = 0
n2 = 1
soma = 0

while limite < n:
    print(soma, end=" -> ")
    soma = n1 + n2
    n2 = n1
    n1 = soma
    limite += + 1
print('FIM')