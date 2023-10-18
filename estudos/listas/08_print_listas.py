'''
Print de Listas
2 Opções:

print "normal"
método join -> texto.join(lista) # texto é o delimitador
'''

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
print(produtos)

print('\n'.join(produtos))
print(', '.join(produtos))

'''
 Lembrando do método split
 lista = texto.split(separador)
'''
# lista = produtos.slit(',') (deleta a virgula, separa e mantem o restante- sobra um espaço) e transforma em lista
lista = produtos.slit(', ') # tira virgula e espaço
