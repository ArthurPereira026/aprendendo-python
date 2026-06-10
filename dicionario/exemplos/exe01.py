dados_pessoais = {

    "nome" : "João",
    "idade" : 21,
    "nascimento" : "20-05-2005",
    "sexo" : "M",
    "altura" : 1.70,
    "temCNH" : True

}


dados_pessoais["peso"] = 70
nova_chave, novo_valor = input("Digite uma nova chave e valor separado por (,) ou atualize algum dado existente: ").split(",")
dados_pessoais[nova_chave] = novo_valor

print(dados_pessoais.keys())

continuar = "s"


while continuar == "s":
    dados = input("Digite o dado que deseja procurar aq: ")
    print(dados_pessoais.get(dados,"Dado não encontrado"))
    continuar = input("Deseja continuar (s/n): ").lower()[0]
    if continuar == "n":
        print("obrigado por usar nosso banco de dados!")