"""
Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h

"""
aviao = 600
carro = 100
onibus = 80

km_percurso = float(input("Informe a quilometragem do percurso: "))

tempo_aviao = km_percurso/aviao
tempo_carro = km_percurso/carro
tempo_onibus = km_percurso/onibus

print(f'Tempo de viagem de aviao: {tempo_aviao:.2f} horas.\n')
print(f'Tempo de viagem de carro: {tempo_carro:.2f} horas.\n')
print(f'Tempo de viagem de onibus: {tempo_onibus:.2f} horas.')
