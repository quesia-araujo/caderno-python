'''
Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique:

Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente
Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido
'''

nome = input("Insira um nome: ")
email = input("insira um email válido")
if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor: # quando o find não encontra, retorna -1
        print('Cadastro concluído') 
else:
    print('Digite seu nome e email corretamente')

'''
if '@' in email:
    posicao = email.find("@")
    subemail = email[posicao:]
    if  '.' in subemail:
        email_valido = True
else:
    email_valido = False 

'''
