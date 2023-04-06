# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input('Qual é a temperatura atual em Celcius? '))
fahrenheit = (temperatura * (9/5)) + 32

print(f'A temperatura {temperatura}ºC em Fahrenheit é: {fahrenheit}ºF.')