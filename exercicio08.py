valorTotalCompras = float(input("Digite o valor das suas Compras aqui: ").replace("," , "."))

if valorTotalCompras <= 100:
    print(f"Você não tem desconto. Sua compra foi de{valorTotalCompras}")

elif valorTotalCompras > 100 and valorTotalCompras <= 300:
    valorDesconto = valorTotalCompras * 0.05
    valorComDesconto = valorTotalCompras - valorDesconto
    print(f"Você teve um desconto de 5% no valor de {valorDesconto:.2f}.O valor total das suas compras foi de {valorComDesconto:.2f}.")

elif valorTotalCompras > 300 and valorTotalCompras < 500:
    print(f"Você teve um desconto de 10% no valor de {valorTotalCompras*0.1:.2f}.O valor total das suas compras foi de {valorTotalCompras*0.9:.2f}.")

elif valorTotalCompras >=500:
    valorDesconto = valorTotalCompras * 0.15
    valorTotalCompras*=0.85
    print(f"Você teve um desconto de 15% no valor de {valorDesconto:.2f} , O total das suas compras foi de {valorTotalCompras:.2f}")