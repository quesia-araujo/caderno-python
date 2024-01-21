"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
"""
def converte_dolar(real,dolar):
    print(f'{real/dolar} dolares')

def converte_peso(real,peso):
    print(f'{real/peso} pesos')

def converte_dolar_australiano(real,dolar_australiano):
    print(f'{real/dolar_australiano} dolar australiano')

def converte_dolar_canadense(real, dolar_canadense):
    print(f'{real/dolar_canadense} dolar canadense')

def converte_franco(real, franco):
    print(f'{real/franco} francos')

def converte_euro(real, euro):
    print(f'{real/euro} euros')

def converte_libra(real, libra):
    print(f'{real/libra} libras')


dolar = 4.91
peso = 0.02
dolar_australiano = 3.18
dolar_canadense = 3.64
franco = 0.42
euro = 5.36
libra = 6.21

real = float(input('Qual o valor em reais? '))
converte_dolar(real,dolar)
converte_dolar_australiano(real, dolar_australiano)
converte_dolar_canadense(real, dolar_canadense)
converte_peso(real,peso)
converte_franco(real,franco)
converte_euro(real,euro)
converte_libra(real,libra)