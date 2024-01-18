"""Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado"""
nota = int(input('Informe uma nota do aluno (entre zero e dez): '))

while nota < 0 or nota > 10:
    print('NOTA INVALIDA.')
    nota = int(input('Por favor, informe uma nota entre zero e dez: '))

if nota >= 7:
    print('Aluno APROVADO.')
else:
    print('Aluno REPROVADO.')
