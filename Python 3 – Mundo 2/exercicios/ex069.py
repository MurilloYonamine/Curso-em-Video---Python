# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

qtd = 0
qtdMulheres = 0
qtdHomens = 0
maiorIdade = 0
cadastros = 0
while True:
    print('---' * 10)
    print('     CADASTRE UMA PESSOA')
    print('---' * 10)

    idade = int(input(f'Qual a idade da {qtd + 1}º pessoa? '))
    sexo = input(f'E o seu sexo [M/F]? ').upper()

    if idade >= 18:
        maiorIdade = maiorIdade + 1

    if idade < 20 and sexo == "F":
        qtdMulheres = qtdMulheres + 1

    if sexo == "M":
        qtdHomens = qtdHomens + 1

    print('---' * 10)
    escolha = input('Você quer continuar [S/N]? ').upper()

    if escolha == "N":
        break
    else:
        qtd = qtd + 1

print(f'Total de pessoas com mais de 18 anos: {maiorIdade}!')
print(f'Ao todo temos {qtdHomens} homem cadastrados!')
print(f'E temos {qtdMulheres} mulheres com menos de 20 anos!')
