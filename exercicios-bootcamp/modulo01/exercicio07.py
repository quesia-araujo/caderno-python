"""
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
"""
peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))

print('Calculando seu IMC...\n')

imc = peso / (altura*altura)

print(f'Seu IMC é de: {imc:.2f}')
