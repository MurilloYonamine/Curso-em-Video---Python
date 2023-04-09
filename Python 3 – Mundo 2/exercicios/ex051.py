# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

print('=' * 30 +
      '\n     10 TERMOS DE UMA PA' +
      '\n' + '=' * 30)

n = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(1, 11):
    pa = n + (c - 1) * razao
    print(pa, end=' -> ')
print('Acabou')