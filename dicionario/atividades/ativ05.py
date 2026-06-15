palavras = {}

frase =  input("Digite frase aqui: ").split()
for n in frase:
    if n not in palavras:
        palavras[n] = 1
    else:
        palavras[n] += 1
for i,j in palavras.items():
    print(f"{i} -> {j}")
