salario_bruto = float('Informe seu salário bruto: ')

if salario_bruto <= 1903.98:
    print('Insento de imposto de renda')
    aliquota = 0
elif salario_bruto <=2826.65:
    aliquota = 7.5
elif salario_bruto <= 3751.05:
    aliquota = 15
elif salario_bruto <= 4664.68:
    aliquota = 22.5
else:
    aliquota = 27.5

desconto = salario_bruto * (aliquota/100)
salario_liquido = salario_bruto - desconto


print(f'O valor do salario líquido eh {salario_liquido}')