carrinho = []
continuar = "continuar"
while continuar == "continuar".lower():
    listaDeCompras = input("O que você quer adicionar a sua lista de compras: ")
    if listaDeCompras == "sair":
        break

    carrinho.append(listaDeCompras)
    carrinho.sort()

print(carrinho)
