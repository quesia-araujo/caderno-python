"""
Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0
"""
qnt_notas = 4
qnt_alunos = 5
lista_media = []
aprovados = 0

for aluno in range(qnt_alunos):
    soma = 0
    for nota in range(qnt_notas):
        print(f'Informe a nota {nota + 1} do aluno {aluno + 1}')
        x = int(input())
        soma += x 
    media = soma/qnt_notas
    lista_media.append(media)
    if media >= 7:
        aprovados +=1

print(lista_media)
print(f'Numero de aprovados: {aprovados}')