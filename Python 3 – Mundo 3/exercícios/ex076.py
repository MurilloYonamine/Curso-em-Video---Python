# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('---' * 20)
print('  ' * 10 + 'LISTAGEM DE PREÇOS')
print('---' * 20)

tupla = ('Lápis' + '..............................................' + 'R$   1.75',
         'Borracha' + '...........................................' + 'R$   2.00',
         'Caderno' + '............................................' + 'R$  15.90',
         'Estojo' + '.............................................' + 'R$  25.00',
         'Transferidor' + '.......................................' + 'R$   4.20',
         'Compasso' + '............................................' + 'R$  9.99',
         'Mochila' + '............................................' + 'R$ 120.32',
         'Canetas' + '............................................' + 'R$  22.30',
         'Livros' + '.............................................' + 'R$  34.90',
         )

for c in range(0, len(tupla)):
    print(tupla[c])
