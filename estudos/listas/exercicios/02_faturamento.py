'''
Faturamento do Melhor e do Pior Mês do Ano
Qual foi o valor de vendas do melhor mês do Ano? E valor do pior mês do ano?
'''
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set','out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

#Juntando listas
vendas_ano = vendas_1sem + vendas_2sem

#Encontrando o maior e menor valor
maior_venda = max(vendas_ano)
menor_venda = min(vendas_ano)

#Encontrando os meses correspondentes
i = vendas_ano.index(maior_venda)
mes_maior = meses[i]
i= vendas_ano.index(menor_venda)
mes_menor = meses[i]

# saída
print('O melhos mês do ano foi {} com {} vendas'.format(mes_maior, maior_venda))
print('O pior mês do ano  foi {} com {} vendas'.format(mes_menor, menor_venda))

top3 = []
top3.append(maior_venda)
vendas_ano.remove(maior_venda)

maior_venda = max(vendas_ano)
top3.append(maior_venda)
vendas_ano.remove(maior_venda)

maior_venda = max(vendas_ano)
top3.append(maior_venda)
print(top3)
