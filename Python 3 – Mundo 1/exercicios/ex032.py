# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime

ano = int(input('Que ano será analisado? '))

if ano % 4 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')

