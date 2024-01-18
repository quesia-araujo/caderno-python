"""O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos."""
numeros_pares = 0
numeros_impares = 0

while True:
    entrada = input("Informe um número (digite 0 para encerrar): ")

    if entrada.isdigit():
        numero = int(entrada)

        if numero == 0:
            break  # Encerra o loop se o usuário informar 0

        if numero > 0:
            if numero % 2 == 0:
                numeros_pares += 1
            else:
                numeros_impares += 1
        else:
            print("Por favor, informe apenas números positivos.")
    else:
        print("Por favor, informe um número válido.")

print(f"Quantidade de números pares: {numeros_pares}")
print(f"Quantidade de números ímpares: {numeros_impares}")
