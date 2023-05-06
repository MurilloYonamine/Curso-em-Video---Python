#  Crie um programa que vai ler vários números e colocar em uma lista.
#  Depois disso, mostre:
#  A) Quantos números foram digitados.
#  B) A lista de valores, ordenada de forma decrescente.
#  C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    escolha = str(input('Deseja Continuar? [S/N]: ')).upper()

    while escolha not in 'SN':
        escolha = str(input('Tente Novamente. Deseja Continuar? [S/N]')).upper()

    if escolha == 'N':
        break

print(f'Foram digitados {len(lista)} números.')
print(f'A lista em forma decrescente é: {sorted(lista, reverse=True)}.')
print("O valor 5 está na lista" if 5 in lista else "Não há o valor 5 dentro da lista!")
