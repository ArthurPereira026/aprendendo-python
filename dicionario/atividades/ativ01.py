pessoa = {
    "nome" : "Arthur",
    "idade" : 18,
    "cidade" : "São Sebastião"
}

for chave, valor in pessoa.items():
    if chave == "nome" or chave == "cidade":
        print(f"{chave} -> {valor}")