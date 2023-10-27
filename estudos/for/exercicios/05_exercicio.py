meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
# [Primeira forma] Criando uma lista auxiliar
acima_meta = []

for venda in vendas:
    if venda[1] >= meta:
        acima_meta.append(venda)

print( '{:.0%} dos vendedores bateram a meta'.format(len(acima_meta)/len(vendas)))

#[Segunda forma] Variável auxiliar
qtde_vendedor_acima = 0

for venda in vendas:
    if venda[1] >= meta:
        qtde_vendedor_acima += 1

print( '{:.0%} dos vendedores bateram a meta'.format(qtde_vendedor_acima/len(vendas)))


# maior venda
vendedor = ''
maior_venda = 0

for venda in vendas:
    if venda[1] > maior_venda:
        maior_venda = venda[1]
        vendedor = venda[0]

print(maior_venda)
print(vendedor)