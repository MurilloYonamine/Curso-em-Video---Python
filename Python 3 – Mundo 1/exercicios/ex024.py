# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite o nome de um cidade: ')
corte = cidade.upper().split()

if corte[0].find("SANTO") == -1:
    print(f'A cidade {cidade} não começa com "Santo" no nome.')
else:
    print(f'A cidade {cidade} não começa com "Santo" no nome.')


