"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721."""

def reverso(num):

    numero_invertido_str = num[::-1]
    numero_invertido = int(numero_invertido_str)
    return numero_invertido


num = input('Informe um número: ')

num_invertido = reverso(num)

print(f'numero original {num}, numero invertido {num_invertido}')