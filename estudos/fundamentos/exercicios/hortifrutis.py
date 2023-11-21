# Função que verifica se a fruta já está na lista e retorna o preço se encontrada
def verifica_fruta(nova_fruta, lista_frutas):
    for fruta in lista_frutas:
        if fruta[0] == nova_fruta:
            return fruta[1]
    return False

# Função para cadastrar novas frutas e seus preços na lista
def cadastro_fruta(n, lista_frutas):
    contador = 0

    # Loop para cadastrar n frutas
    while contador < n:
        nova_fruta = input('Informe o nome da fruta: ')

        # Loop enquanto a fruta já estiver cadastrada
        while verifica_fruta(nova_fruta, lista_frutas):
            print("Produto já cadastrado cadastrado")
            nova_fruta = input('Informe o nome da fruta: ')

        preco = input('Informe o preço da fruta: ')
        lista_frutas.append([nova_fruta, preco])
        contador += 1

# Função para imprimir a lista de frutas cadastradas
def imprimir_lista_frutas(lista_frutas):
    for fruta in lista_frutas:
        print(fruta)

# Função para buscar e imprimir o preço de uma fruta específica
def busca_fruta(fruta, lista_frutas):
    for item in lista_frutas:
        if item[0] == fruta:
            print(item[1])
            return
    print("Produto não cadastrado")

# Lista inicial de frutas
lista_frutas = []

# Solicita a quantidade de frutas a serem cadastradas
n = int(input('Informe a quantidade de itens a ser cadastrado: '))

# Chama a função de cadastro de frutas
cadastro_fruta(n, lista_frutas)

# Solicita o nome da fruta para buscar o preço
nome = input('Informe qual fruta deseja consultar o preço: ')

# Chama a função de busca e imprime o resultado
busca_fruta(nome, lista_frutas)

# Comentado para não imprimir a lista completa de frutas no final
# imprimir_lista_frutas(lista_frutas)
