# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = input('Qual é o seu nome? ')
primeiroNome = nome.split()

print(f'Nome em maiúsculo: {nome.upper()}. \n'
      f'Nome em minúsculo: {nome.lower()}. \n'
      f'Quantidade de letras: {len("".join(nome.split()))}. \n'
      f'Quantidade de letras primeiro nome: {len(primeiroNome[0])}')