# Crie um programa que tenha uma dupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

n = int(input('Digite um número entre 0 e 20: '))

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while n > 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {extenso[n]}!')
