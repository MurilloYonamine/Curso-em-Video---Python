# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input('Qual é o valor em metros? '))

cm = m * 100
mm = m * 1000

print(f'A medida {m} m é igual a: {cm} cm e {mm} mm')
