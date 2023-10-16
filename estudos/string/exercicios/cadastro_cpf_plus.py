'''
Agora, além das validações anteriores, vamos criar um input que permita que o usuário insira pontos, traços e inclusive espaços vazios.

Nosso programa deve "tratar" o que o usuário inserir para padronizar o CPF dele em apenas números.

A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços do CPF que o cliente inserir e, uma vez retirados pontos, traços e espaços, devem sobrar apenas números no CPF. Qualquer outro caractere deve ser considerado inválido.

No final, nosso programa deve exibir uma mensagem para o usuário, caso ele tenha inserido o CPF inválido ou então apenas deve printar o CPF correto já só com número.

'''

cpf_invalido = True

while(cpf_invalido):
    cpf = input("insira seu cpf (digite apenas números)")

    # tirando os espaços do início e final
    cpf = cpf.strip()
    # tirando os . (pontos), - (traços) e espaços
    cpf = cpf.replace('.','')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')

    if len(cpf) == 11 and cpf.isnumeric:
        print(cpf)
        cpf_invalido = False
    else:
        print("Digite seu cpf corretamente e digite apenas números")