n = int(input("Digite um número inteiro: "))

ind = True
soma = 0

while(ind):
    digito = n % 10
    n = n // 10
    soma = soma + digito
    if digito == 0 and n < 1:
        ind = False
print(soma)