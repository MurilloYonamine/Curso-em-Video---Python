# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Informe o seu sexo: [M/F] ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos. Por favor, informe o sexo novamente: ').upper()

if sexo == 'M':
    print('Sexo masculino registrado.')
if sexo == 'F':
    print('Sexo feminino registado.')
