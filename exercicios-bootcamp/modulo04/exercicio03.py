""" Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função.
"""

def celsius_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit
    
def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def menu():
    print('Conversão de temperatura')
    opcao = int(input('1 - Celsius para Fahrenheit\n2 - Fahrenheit para Celsius\n'))

    if opcao == 1:
        celsius = float(input('Informe a temperatura em Celsius'))
        temperatura_fahrenheit = celsius_fahrenheit(celsius)
        print(f'{temperatura_fahrenheit} F')
    elif opcao == 2:
        fahrenheit = float(input('Informe a temperatura em Fahrenheit'))
        temperatura_celsius = fahrenheit_celsius(fahrenheit)
        print(f'{temperatura_celsius} C')
    else:
        print('Opção Invalida')


menu()