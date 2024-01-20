"""
Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
"""
perguntas = [
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Mora perto da vítima?',
    'Devia para a vítima?', 
    'Já trabalhou com a vítima?' 
]

contador = 0

for pergunta in perguntas:
    print(pergunta)
    resposta = input('S - sim\nN - não\n')
    if resposta == 'S':
        contador += 1

print('Classificador: ')

if contador <2:
    print('Inocente')
elif contador == 2:
    print('Suspeita')
elif contador <=4:
    print('Cumplice')
else:
    print('Assassino')
