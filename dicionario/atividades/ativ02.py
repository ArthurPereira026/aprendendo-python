dados_pessoais = {

    "nome" : "João",
    "idade" : 21,
    "nascimento" : "20-05-2005",
    "sexo" : "M",
    "altura" : 1.70,
    "temCNH" : True

}

dados_pessoais["idade"] = 29
dados_pessoais["profissão"] = "Eletricista"

for chave, valor in dados_pessoais.items():
    print(f"{chave} -> {valor}")