print("Olá seja bem vindo a nossa área de autoatendimento da nossa lanchonete Spudz\nEsse é o nosso cardapio dísponivel de hoje: \n Cachorro-Quente: Código -> 100\n Bauru Simples: Código -> 101 \n X-Salada: Código -> 102 \n Hambúrguer: Código -> 103 ")
while True:
    pedido =  int(input("Faça seu pedido digitando o código do seu prato desejado: "))
    match pedido:
        case 100:
            print("Você escolheu o Cachorro quente no valor de R$ 10,00")
            pedido = input("Deseja Pedir mais alguma coisa? (S/N): ").upper()
            if pedido == "N":
                print("Obrigado por comprar no Spudz, Volte sempre!!")
                break
        case 101:
            print("Você escolheu o Bauru Simples no valor de R$ 12,00")
            pedido = input("Deseja Pedir mais alguma coisa? (S/N): ").upper()
            if pedido == "N":
                print("Obrigado por comprar no Spudz, Volte sempre!!")
                break
        case 102:
            print("Você escolheu o X-Salada no valor de R$ 15,00")
            pedido = input("Deseja Pedir mais alguma coisa? (S/N): ").upper()
            if pedido == "N":
                print("Obrigado por comprar no Spudz, Volte sempre!!")
                break
        case 103:
            print("Você escolheu o Hambúrguer no valor de R$ 13,00")
            pedido = input("Deseja Pedir mais alguma coisa? (S/N): ").upper()
            if pedido == "N":
                print("Obrigado por comprar no Spudz, Volte sempre!!")
                break
        case _:
            print("Por favor selecione um produto Valido")
