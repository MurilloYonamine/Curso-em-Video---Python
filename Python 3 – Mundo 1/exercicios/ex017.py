# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

oposto = float(input('Qual é o cateto oposto? '))
adjacente = float(input('Qual é o cateto adjacente? '))

hipotenusa = math.hypot(oposto, adjacente)

print(f'O cateto oposto é: {oposto};\n'
      f'O cateto adjacente é: {adjacente};\n'
      f'Logo, sua hipotenusa é: {hipotenusa:.2f}.')
