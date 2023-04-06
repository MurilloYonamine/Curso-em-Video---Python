# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².

larg = float(input('Qual é a largura da parede? '))
alt = float(input('Qual é a altura da parede? '))

area = larg * alt
tinta = area / 2

print(
    f'A área de sua parede, com a largura de {larg:.2f}m e altura de {alt:.2f}m, é: {area:.2f}m². Portanto será necessário {tinta:.2f}L.')
