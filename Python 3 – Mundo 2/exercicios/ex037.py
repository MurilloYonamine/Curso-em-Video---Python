# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
import math

n = int(input('Digite um valor: '))

print("""
Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
""")
opcao = int(input('Sua opção: '))

if opcao > 3:
    print('Está fora do intervalo de números!')
elif opcao == 1:
    bin = format(n, "b")
    print(f'{n} convertido para Binário é igual a: {bin}')
elif opcao == 2:
    octal = format(n, "o")
    print(f'{n} convertido para Octal é igual a: {octal}')
else:
    hex = format(n, "x")
    print(f'{n} convertido para Octal é igual a: {hex}')
