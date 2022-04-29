#Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

while True:
    print("Opções disponíveis:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multicação")
    print("0 - Saída")
    opcao = int(input("Informe a opção desejada ou 0 para sair: "))
    
    tabuada = 1
    
    if opcao == 0:
        break
    
    elif opcao == 1:
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} + {numero} = {tabuada + numero}")
                numero += 1
            tabuada += 1
    
    elif opcao == 2:
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{numero} - {tabuada} = {numero - tabuada}")
                numero += 1
            tabuada += 1
    
    elif opcao == 3:
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{numero} / {tabuada} = {numero / tabuada}")
                numero += 1
            tabuada += 1
    
    elif opcao == 4:
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} x {numero} = {tabuada * numero}")
                numero += 1
            tabuada += 1
    else:
        print("Opção inválida, tente novamente.")
