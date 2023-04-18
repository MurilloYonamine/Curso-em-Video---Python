# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = int(input('Digite um número: '))
c = input('Quer continuar? [S/N]: ').upper()
soma = 0
qtd = 0

while c != 'S' and c != 'N':
    print(f'{c} não é um parâmetro')
    c = input('Digite corretamente. VOcê deseja continuar? [S/N]: ').upper()

maior = n
menor = n
soma = soma + n
qtd = qtd + 1

while c == 'S':
    n = int(input('Digite um número: '))
    c = input('Quer continuar? [S/N]: ').upper()
    soma = soma + n
    qtd = qtd + 1
    if n > maior:
        maior = n
    else:
        menor = n

media = soma / qtd
print(f'Você digitou {qtd} números e a média foi: {media}')
print(f'O maior valor foi: {maior}. E o menor foi: {menor}')
