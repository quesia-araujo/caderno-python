'''
Alterações "Incrementais" de Variáveis
Estrutura:

variavel = variavel + outro_valor
ou então

variavel += outro_valor
'''

lista = ['mac', 'iphone']
vendas = [100, 200]

#adicionando IPad na lista
lista += ['Ipad']
print(lista)

soma_vendas = 300

#adicionando na soma a quantidade de IPad
soma_vendas += 500

# Incremento com string
email = 'Esse mês vendemos um total de {} produtos, sendo:\n{} unidades de {}\n{} unidades de {}'.format(soma_vendas, vendas[0], lista[0], vendas[1], lista[1])
#adicionando no fim do texto o Ipad

email += '\n{} unidades de Ipad'.format(500)

print(email)