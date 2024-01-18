"""10. Faça um programa que lê três números inteiros e os mostra em ordem
crescente."""

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))


if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

print(f"Números em ordem crescente: {num1}, {num2}, {num3}")
