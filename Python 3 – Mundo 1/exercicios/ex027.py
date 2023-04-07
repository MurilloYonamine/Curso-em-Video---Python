# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Qual é o seu nome completo? ').strip()

lista = nome.split()
primeiroNome = lista[0]
ultimoNome = lista[::-1]

print(f'Seja Bem Vindo! {ultimoNome[0]}, {primeiroNome}.')