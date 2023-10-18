'''
Algumas Funções Básicas de Lista

Tamanho da Lista

tamanho = len(lista)
'''

produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']

tamanho = len(produtos)

print('temos {} produtos'.format(tamanho))

'''
Maior e Menor Valor
maior = max(lista)

menor = min(lista)
'''

vendas = [1000, 1500, 15000, 270, 900, 100, 1200]
mais_vendido = max(vendas)
menos_vendido = min(vendas)

print('O produto mais ventido teve {} unidades vendidas. O menos vendido teve {} vendas'.format(mais_vendido, menos_vendido))

i_mais = vendas.index(mais_vendido)
i_menos = vendas.index(menos_vendido)

print('O produto mais vendido foi {}'.format(produtos[i_mais]))
print('O produto menos vendido foi: {}'.format(produtos[i_menos]))