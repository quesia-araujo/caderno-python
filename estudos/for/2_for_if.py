vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000
bateu_meta = 0
total_vendas = len(vendas)

for item in vendas:
    if item > meta:
        bateu_meta += 1

porcentagem = (bateu_meta / total_vendas) * 100

print( '{} Funcionários bateram a meta. {:.1%}'.format(bateu_meta, porcentagem))