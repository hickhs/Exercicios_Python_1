#Programa para converter dias, horas, minutos e segundos para um total de segundos.

#Entradas e declaração de variáveis
dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Por fim, informe a quantidade de segundos: "))

#Processamento (Cálculos)
segundos_dias = (((dias * 24) * 60) * 60)
segundos_horas = ((horas * 60) * 60)
segundos_minutos = minutos * 60
segundos_totais = segundos_dias + segundos_horas + segundos_minutos + segundos

#Saída
print(f"O total de segundos é: {segundos_totais}")