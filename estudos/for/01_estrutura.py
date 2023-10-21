'''Funcionamento:
for i in range(n)
    repetir codigo n vezes
'''
for i in range(5):
    print(i)

'''
Imagine que você está construindo uma automação para enviar todo dia por e-mail um resumo da produção de uma fábrica. Construa um código que exiba a quantidade produzida de cada os produto nesse "e-mail"
'''

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

tamanho = len(produtos)
for i in range(tamanho):
    print('{} unidade produzidas de {}'.format(producao[i], produtos[i]))