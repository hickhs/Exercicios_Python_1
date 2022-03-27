#Programa para calcular o tempo de uma viagem

#Entradas e declaração de variáveis
distancia = float(input("Informe a distância da viagem em km: "))
velocidade = float(input("Informe a velocidade média esperada para a viagem em km/h: "))

#Processamento
tempo_gasto = distancia / velocidade

#Saída
print(f"O tempo da viagem será de {tempo_gasto:.1f} horas")