def divisao(a, b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("Erro: Impossível dividir um valor por zero.")
    except TypeError as e:
        print(f'Erro: O tipo do dado informado está incorreto.\nDetalhes: {e}')
    else: 
        print('Sem excessões')

divisao(10,2)
#divisao(10, "womakerscode")

