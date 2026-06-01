while True:
    print("1 = Soma")
    print("2 = Subtrair")
    print("3 = Multiplicar")
    print("4 = Dividir")
    print("5 = Sair")

    opcao = int(input("Escolha uma das opções acimas: "))

    if opcao == 1:
        numero = float(input("Digite seu numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        print(numero + numero2)

        opcao = input("Quer continuar? (s/n) ").upper()[0]

    elif opcao == 2:
        numero = float(input("Digite seu numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        print(numero - numero2)
        opcao = input("Quer continuar? (s/n) ").upper()[0]

    elif opcao == 3:
        numero = float(input("Digite seu numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        print(numero * numero2)
        opcao = input("Quer continuar? (s/n) ").upper()[0]

    elif opcao == 4:
        numero = float(input("Digite seu numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        if numero2 == 0:
            print("Nenhum número pode ser divisivel por 0")
            numero2 = float(input("Digite um segundo número válido: "))
        print(numero / numero2)
        opcao = input("Quer continuar? (s/n) ").upper()[0]

    elif opcao == 5:
        print("fechando...")
        break