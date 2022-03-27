#Escreva um programa que lei três números e imprima o maior e o menor

#Entradas e declaração de variáveis
from this import d


primeiro = int(input("Insira um número: "))
segundo = int(input("Insira outro número: "))
terceiro = int(input("Por fim, insira um último número: "))

#Processamento
maior = primeiro

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

menor = primeiro

if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

print(f"O maior número é {maior} e o menor número é {menor}")