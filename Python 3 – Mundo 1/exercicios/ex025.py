# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Qual é o seu nome? ')

if nome.upper().find("SILVA") == -1:
    print('Você não tem "Silva" no nome.')
else:
    print('Você tem "Silva" no nome.')
