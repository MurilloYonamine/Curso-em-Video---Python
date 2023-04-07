# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite um valor: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Seno: {seno:.2f}\n'
      f'Cosseno: {cosseno:.2f}\n'
      f'Tangente: {tangente:.2f}.')