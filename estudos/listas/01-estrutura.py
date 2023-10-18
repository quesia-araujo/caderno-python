''' ESTRUTURA
lista = [valor, valor, valor]
posso ter uma variável como valor tbm
'''

produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
vendas = [1000, 1500, 350, 270, 900]

'''
lista[i] eh o valor do item de índice i da lista
'''

print(produtos[1]) # imprimirá celular

print('Vendas do produto {} foram de {} unidades' .format(produtos[1], vendas[1]))

'''
modificar um item da lista
'''
vendas[3]= 300
print(vendas[3])

'''
Diferença entre string e lista:
string é imutável,  lista não.
----exemplo--- não é possível
texto = 'Quesia'
texto[1] = i
-------------- 
para fazer essa mudança é necessário usar a função replace
'''
texto = 'Quesia'
texto = texto.replace('u', 'i')

