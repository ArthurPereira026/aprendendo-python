while True:
    print("Operações: \n 1 - SOMAR \n 2 - SUBTRAIR \n 3 - MULTIPLICAR \n 4 - DIVIDIR \n 5 - SAIR ")
    opcao = int(input("Escolha a operação que deseja realizar: "))

    match opcao:
        case 1:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            result = num1 + num2
            print(f"O resultado é: {result}")
        case 2:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            result = num1 - num2
            print(f"O resultado é: {result}")
        case 3:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            result = num1 * num2
            print(f"O resultado é: {result}")
        case 4:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            if(num2 == 0):
                print("Não é possível dividir nenhum número por Zero.")
                continue
            result = num1 / num2
            print(f"O resultado é: {result}")
        case 5:
            break
        case _:
            print("Escolha uma das opções disponíveis")