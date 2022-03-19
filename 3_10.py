#Programa para calcular o aumento de um salário

#Entradas e declaração de variáveis
salario_atual = float(input("Informe o valor do salário atual: "))
taxa_percentual = float(input("Informe a taxa percentual do aumento: "))

#Processamento
aumento = ((taxa_percentual / 100) * salario_atual)
novo_salario = aumento + salario_atual

#Saída
print(f"O valor do aumento é de: R$ {aumento:.2f}")
print(f"O valor do novo salário é de: R$ {novo_salario:.2f}")