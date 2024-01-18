"""
Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício
"""
horas_semana = float(input('Quantas horas de exercício fisico realiza por semana? '))

minutos_por_mes = horas_semana *4 *60

calorias_gastas = minutos_por_mes * 5

print(f'As calorias gastas durante o mes: {calorias_gastas:.2f}')