# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip()

print(f'A letra "A" aparece {frase.upper().count("A")} vezes na sua frase.')

primeira = frase.upper().find("A")

segunda = frase.upper().rfind("A")

print(f'Ela aparece pela primeira vez na posição: {primeira}. \n'
      f'Ela aparece pela última vez na posição: {segunda}.')
