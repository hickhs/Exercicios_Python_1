#Entrada e declaração de variáveis
salario = float(input("Informe o valor do salário: "))

#Processamento
if salario <= 1250.00:
    aumento = salario * 0.15

if salario > 1250.00:
    aumento = salario * 0.1

#Saída
print(f"O valor do aumento é de R$ {aumento:.2f}")