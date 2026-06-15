estoque = {
    "Teclado": 15,
    "Mouse": 22,
    "Monitor": 8
}
print(estoque)
continuar = "continuar"
while continuar == "continuar":
    nome, quantidade = input("""
     Bem Vindos a Café impresso ☕
     Digite o Nome do Produto e a Quantidade que deseja comprar,
     separando-a por virgula: """).split(",")
    retorno = estoque.get(nome, "Produto n encontrado!")

    for chave, valor in estoque.items():
        if nome.lower() == chave.lower():
            if valor == 0:
                print("Infelizmente o estoque desse produto estar esgotado😥😥😥")
                continue
            if valor < int(quantidade):
                print("Possuímos esse item no estoque,Mas infelizmente temos menos do que desejas")
                continue
            else:
                estoque[chave] -= int(quantidade)
                atualiza_estoque = True

    if atualiza_estoque:
        print("Este é o nosso estoque atual atualizado!")
        for chave, valor in estoque.items():
            print(f"{chave} -> {valor}")

    continuar = input("Desejas Continuar a sua compra ou quer ir para o carrinho? (continuar/carrinho): ").lower()
else:
    print("Agradecemos por comprar na Café impresso ☕")




