# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
import random

tentativas = 0
lista = random.randint(0, 10)

print('O computador pensou em um número no intervalo de 0-10.')
palpite = int(input('Qual o seu palpite? '))

while palpite != lista:
    tentativas += +1
    if palpite < lista:
        palpite = int(input('Errado! Um pouco mais.\nQual o seu novo palpite? '))
    else:
        palpite = int(input('Errado! Um pouco menos.\nQual o seu novo palpite? '))

print(f'Isso, é o número {palpite}! Você acertou depois de {tentativas} tentativas!')
