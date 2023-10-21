qtde_pessoas = int(input('Quantas pessoas terão no quarto'))
quarto = []

for i in range(qtde_pessoas):
    nome = input('Qual nome?')
    cpf = input('Qual cpf?')
    hospede = [nome, 'cpf: {}'.format(cpf)]
    quarto.append(hospede)

print(quarto)
