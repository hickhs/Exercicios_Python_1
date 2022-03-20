#Programa para calcular valor de aluguel de carro

#Entradas e declaração de variáveis
km = float(input("Informe a distância percorrida pelo carro em km: "))
dias = float(input("Informe a quantidade de dias pelos quais o carro foi alugado: "))

#Processamento
aluguel = (60 * dias) + (0.15 * km)

#Saídas
print(f"O valor a ser pago pelo aluguel é de: R$ {aluguel:.2f}")