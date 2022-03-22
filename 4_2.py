#Programa para calcular multa

#Entrada e declaração de variáveis
velocidade = float(input("Informe a velocidade do carro: "))

#Processamento
if velocidade > 80:
    valor_multa = (velocidade - 80) * 5
    print(f"Você foi multado em R$ {valor_multa:.2f}.")
if velocidade <= 80:
    print("Você não foi multado.")
    