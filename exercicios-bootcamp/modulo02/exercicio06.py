"""Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.
"""
login = input("Digite o login: ")
senha = input("Digite a senha: ")


if login == "admin" and senha == "admin123":
    print("Acesso permitido. Bem-vindo, admin!")
else:
    print("Credenciais incorretas. Acesso negado.")