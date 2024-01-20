""" Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
"""

carrinho = {'morango': 3, 'Abacate': 5, 'chocolate': 2}

#values = int(carrinho.values())
total_item = 0
for chave in carrinho:
    total_item += carrinho[chave]

print(f'Quantidade de itens no carrinho eh: {total_item}')