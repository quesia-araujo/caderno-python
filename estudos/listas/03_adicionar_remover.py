'''ADICIONAR
    lista.append(item)
    ***adiciona o item no final da lista***

    REMOVER
    item_removido = lista.pop(indice)
    lista.pop(indice)
    lista.remove(item)
'''

produtos = ['apple tv', 'mac', 'iphone x', 'iPad', 'apple watch', 'mac book', 'airpods']
print(produtos)
# adicionar o IPHONE 11
produtos.append('iphone 11')
print(produtos)

# remover o iphone x
produtos.remove('iphone x')
item_removido = produtos.pop(2)

print('O item removido da lista foi: {}'.format(item_removido))

produto_remover = 'iphonex'

if produto_remover in produtos:
    produtos.remove(produto_remover)
else:
    print('{} não existe na lista de produtos'.format(produto_remover))



