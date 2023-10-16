'''
Crie um programa para fazer uma consulta de estoque. O usuário do programa deve inserir o nome do produto e, caso ele não exista na lista, ele deve ser avisado. Caso exista, o programa deve dizer a quantidade de unidades em estoque do produto
'''

produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet', 'geladeira']
estoque = [100, 150, 100, 120, 70, 80]

produto = input('Informe o produto que procura: ')
produto = produto.casefold() # string em letras minúsculas

if produto in produtos:
    i = produtos.index(produto)
    qtd_estoque = estoque[i]
    print('A quantidade de {} em estoque é {}' .format(produtos[i], qtd_estoque))
else:
    print('Produto informado não existe no estoque.')