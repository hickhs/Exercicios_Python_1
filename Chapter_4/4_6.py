#Entrada e declaração de variáveis
distancia = float(input("Qual a distância que você deseja percorrer em km? "))

#Processamento
if distancia <= 200:
    passagem = distancia * 0.50
    print(f"O preço da sua passagem é de R$ {passagem}")
else:
    passagem = distancia * 0.45
    print(f"O preço da sua passagem é de R$ {passagem}")