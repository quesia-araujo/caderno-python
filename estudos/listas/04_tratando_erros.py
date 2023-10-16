''' FORMAS DE TRATAR O ERRO

1 - Criar um if para evitar que ele aconteça

2- Esperar que ele possa acontecer e tratar caso o erro aconteça
    try:
        tentar fazer
    except:
        caso dê erro
'''

produtos = ['apple tv', 'mac', 'iphone x', 'iPad', 'apple watch', 'mac book', 'airpods']

try:
    produtos.remove('iphonex')
except:
    print('iphonex não existe na lista de produtos')

# Ou ainda:

try:
    produtos.remove('iphonex')
except:
    pass # não faz nada
