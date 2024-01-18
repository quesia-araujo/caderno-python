"""Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês."""

valor_por_hora = float(input('Informe quanto voce fanha por hora: '))
horas_trabalhadas = float(input('Quantas horas trabalha por mes? '))

salario = valor_por_hora * horas_trabalhadas

print(f'Salario recebido: {salario:.2f}')