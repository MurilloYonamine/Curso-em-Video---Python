# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

n = float(input('Digite um número real: '))

print(f'A porção inteira de {n} é: {math.trunc(n)}')