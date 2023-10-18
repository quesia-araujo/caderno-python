'''
Juntar Listas, Ordenar e Cuidados Especiais
2 formas:
lista1.extend(lista2)
lista_nova = lista1 + lista2
Obs: o Método .append não junta listas, mas adiciona um valor no final da lista
'''

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
novos_produtos = ['iphone 12', 'ioculos']

todos_produtos = produtos + novos_produtos
print(todos_produtos)


produtos.extend(novos_produtos) # adiciona como valor, uma lista (lista dentro de lista)
print(produtos)

'''
[1] + [2] não é a mesca coisa que 1 + 2
'''
print([1] + [2])
print(1 + 2)

'''
Ordenar listas:
lista.sort()
'''
vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
vendas.sort()
print(vendas)

todos_produtos.sort() # segue tabela ascii (maiusculas primeiro-tratar com metodo string)
print(todos_produtos)

vendas.sort(reverse=True) # Ordem decrescente
print(vendas)