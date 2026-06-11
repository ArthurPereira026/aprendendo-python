mercadoria = {
    "arroz" : 20.00,
    "feijão" : 15.00,
    "milho" : 5.00,
    "farinha" : 11.00,
    "refrigerante" : 10.00,
    "banana" : 14.50
}
compras = input("Podemos iniciar suas compras? (s/n): ").lower()[0]

while compras == "s":
    carrinho = (input("o que desejas adicionar ao seu carrinho?:  "))
    print(mercadoria.get(carrinho, "Esse item está em falta no momento!"))
    compras = input("Deseja adicionar mais algum item nos eu carrinho? (s/n): ").lower()[0]
    if compras == "n":
        print("Agradecemos a sua preferencia!!")
        break