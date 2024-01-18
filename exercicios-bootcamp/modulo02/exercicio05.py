"""
Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas
"""
print('Informe os tres lados de um triangulo.')
lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if lado1 == lado2 == lado3:
    print('Equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Isosceles')
else:
    print('escaleno')