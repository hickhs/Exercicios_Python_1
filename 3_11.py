#Programa para o calcular o desconto de uma mercadoria

#Entradas e declaração de variáveis
preco = float(input("Informe o preço da mercadoria: "))
percentual_desconto = float(input("Informe a taxa percentual do desconto: "))

#Processamento
desconto = (percentual_desconto / 100) * preco
valor_pagar = preco - desconto

#Saída
print(f"O valor a pagar é de R$ {valor_pagar:.2f}")