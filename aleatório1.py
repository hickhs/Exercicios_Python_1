# Um escritório de contabilidade encomendou um sistema financeiro para os desenvolvedores
# de uma empresa de software. Uma das muitas funções a serem desenvolvidas é a função
# “montante”, que calcula o montante final de aplicações ou empréstimos financeiros
# utilizando juros simples. Construa um algoritmo para calcular o montante dos empréstimos
# financeiros tomados.

#Entradas e declaração de variáveis
aplicado = float(input("Insira o valor aplicado inicialmente: "))
tempo = float(input("De quantos meses é a aplicação? "))
taxa = float(input("Qual a taxa percentual de juros? "))

#Processamento (Cálculo)
montante = (aplicado * (taxa / 100) * tempo) + aplicado

#Saída
print(f"O montante final da aplicação é de R$ {montante:.2f}")