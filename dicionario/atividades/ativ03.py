quadrado = {}

for i in range(1, 6):
    quadrado.setdefault(i,i**2)
for chave, valor in quadrado.items():
    print(f"{chave} -> {valor}")