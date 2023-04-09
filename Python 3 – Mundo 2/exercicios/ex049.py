# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
from time import sleep
n = int(input('Digite um número para saber sua tabuada: '))

for c in range(0, 11):
    print(f'{n} X {c} = {n * c}')
    sleep(0.4)
