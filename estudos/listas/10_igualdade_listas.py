'''
Copiar e "Igualdade" de Listas
Estrutura:
Quando fazemos:
lista2 = lista1
não estamos criando uma lista nova, mas estamos atribuindo outra variável à mesma lista.
Duas listas, apontando para o mesmo endereço
'''

lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista

lista[1] = 'iphone 11'

print(lista)
print(lista2)

'''
Se quisermos copiar lista devemos fazer
lista2 = lista1.copy()
ou entao
lista2 = lista1[:]
'''
lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista[:]

lista[1] = 'iphone 11'
print(lista)
print(lista2)