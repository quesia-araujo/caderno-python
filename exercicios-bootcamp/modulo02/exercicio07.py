""". Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
"""

idade = int(input('Informe sua idade: '))
# criança até os 12 - adolescente até 18, adulto até 60

if idade > 0 and idade < 120:
    if idade < 12:
        print('Você é uma criança.')
    elif idade < 18:
        print('Você é adolescente.')
    elif idade < 60:
        print('Você é adulto.')
    else: 
        print('Você é idoso.')
else:
    print('Idade inválida.')