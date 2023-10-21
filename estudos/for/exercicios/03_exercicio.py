meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for i, venda in enumerate(vendas):
    if venda[1] >= meta:
        print('O vendedor {} bateu a meta com {} vendas'.format(vendas[i][0], vendas[i][1]))