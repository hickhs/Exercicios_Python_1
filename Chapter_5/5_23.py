#Solicitando do usúario um número para ser testado:
numero = float(input("Informe um número: "))

#Informando que tanto 0 quanto 1 não são primos:
if (numero == 0) or (numero == 1):
    print("O número não é primo.")

#Informando que 2 é primo:
#OBS: 2 é o único número primo par.
elif (numero == 2):
    print("O número é primo.")

#Informando que todos os números pares, exceto o 2, não são primos:
else:
    if numero % 2 == 0:
        print("O número não é primo.")
    else:
        impar = 3
        while impar < numero:
            if numero % impar == 0:
                break
            impar += 2
        if impar != numero:
            print("O número não é primo.")
        else:
            print("O número é primo.")
