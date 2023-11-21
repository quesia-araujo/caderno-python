def calcular_combustivel(distancia, consumo_medio):
    return distancia / consumo_medio

# Entrada de Dados
tempo = float(input("Informe o tempo gasto na viagem em horas: "))
velocidade_media = float(input("Informe a velocidade média do veículo em km/h: "))

# Processamento
distancia_percorrida = tempo * velocidade_media

quantidade_combustivel = calcular_combustivel(distancia_percorrida, 1)  # Considerando rendimento de 1 km por litro

# Saída de Dados
print("A quantidade de litros de combustível gasta é:", quantidade_combustivel)