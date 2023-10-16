'''
Dado um item, saber qual posição ele ocupa
i = lista.index('item')
'''
produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet', 'geladeira']
estoque = [100, 150, 100, 120, 70, 80]

i = produtos.index('geladeira')
print(produtos[i])

'''
Descobrir a quantidade de estoque do produto geladeira
'''

qtd_estoque = estoque[i]
print(qtd_estoque)

'''
Crie um programa para fazer uma consulta de estoque. O usuário do programa deve inserir o nome do produto e, caso ele não exista na lista, ele deve ser avisado. Caso exista, o programa deve dizer a quantidade de unidades em estoque do produto
'''

produto = input('Informe o produto que procura: ')

if produto in produtos:
    i = produtos.index(produto)
    qnt_estoque = estoque[i]
    print('A quantidade de {} em estoque é {}' .format(produtos[i], qnt_estoque))
else:
    print('Produto informado não existe no estoque.')