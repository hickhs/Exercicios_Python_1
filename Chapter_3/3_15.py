#Programa para calcular a redução do tempo de vida de um fumante

#Entradas e declaração de variáveis
quant_cigarros_dia = int(input("Informe a quantidade de cigarros fumados por dia: "))
anos = int(input("Informe por quantos anos você já fuma: "))

#Processamento
total_cigarros = (anos * 365) * quant_cigarros_dia
dias_perdidos = (total_cigarros * 10) / 60

#Saída
print(f"O fumante já perdeu {dias_perdidos} dias da sua vida.")