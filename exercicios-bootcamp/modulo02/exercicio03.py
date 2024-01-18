"""
3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido
"""

nota = int(input('Informe uma nota entre zero e dez: '))

while nota < 0 or nota > 10:
    print('Nota inválida.')
    nota = int(input('Por favor, informe uma nota entre zero e dez: '))