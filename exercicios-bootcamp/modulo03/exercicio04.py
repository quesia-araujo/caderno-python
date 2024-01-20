"""Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.

"""
lista_telefonica = {'Adriana': 99249839945, 'Roberta': 99178839934, 'Gabriel': 999999999}

busca = input('Informe o nome que deseja buscar: ')
encontrou = False

for chave in lista_telefonica:
    if busca in chave:
        print(lista_telefonica[chave])
        encontrou = True

if encontrou == False:
    print('Contato não encontrado')
   