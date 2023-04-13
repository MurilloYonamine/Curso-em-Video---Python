#  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.

a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n = 1
t = 0
limite = 11
novoLimite = 0
while n <= limite:
    x = a + (n - 1) * r
    print(x, end=" -> ")
    n = n + 1
    t = t + 1
    if n == limite:
        print('PAUSA')
        novoLimite = int(input('Quantos termos você quer mostrar a mais? '))
        if novoLimite == 0:
            print(f'Progressão aritmética finalizada com {t} termos mostrados.')
            limite = 0
        limite = novoLimite + limite
