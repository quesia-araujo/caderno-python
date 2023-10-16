'''
Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input box apenas com números.

Ex: 'Insira seu CPF (digite apenas números)'

Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"

'''

cpf_invalido = True

while(cpf_invalido):
    cpf = input("insira seu cpf (digite apenas números)")

    if len(cpf) == 11 and cpf.isnumeric:
        print(cpf)
        cpf_invalido = False
    else:
        print("Digite seu cpf corretamente e digite apenas números")