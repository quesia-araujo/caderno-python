import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&().,'
print('Welcome To Your Password Generator')

number = int(input('Amount of passwords to generate: '))
length  = int(input('Input your password length: '))

print('\nHere are your passwords:')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

'''
Gerador de senhas aleatórias.
### Entrada de dados ###
O usuário informa o número de senhas e seus tamanhos

### processsamento de dados ###
A cada iteração do loop interno do for, um caractere aleatório é escolhido da string chars e adicionado à senha.

### Saída de dados ###
É exibido uma coleção de senhas com caracteres aleatórios

Tópicos
 - laços for 
 - módulo random
'''


