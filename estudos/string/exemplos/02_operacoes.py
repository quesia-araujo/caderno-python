faturamento = 1000
custo = 500
lucro = faturamento - custo

# operador + e str 
print ('O faturamento da loja foi de: ' + str(faturamento))

# format (uso recomendado)
print('O faturamento foi de: {} '.format(faturamento))
print('O faturamento foi de: {}, o custo foi  de {} e o lucro foi {} '.format(faturamento, custo, lucro))
print('O faturamento foi de {0}, o custo foi  de: {1} e o lucro foi {2}. Lembrando o faturamento foi: {0} '.format(faturamento, custo, lucro))

# %d(numero) e %s(string)
print ('O faturamento foi de: %d, o custo foi %d e o lucro %d' % (faturamento, custo, lucro))

# uso do in
print('@' in 'quesia@gmail.com')
print('@' in 'quesia.gmail.com')