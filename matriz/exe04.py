matriz_base = [[1, 2], [3, 4]]
fator = int(input("Digite um fator: "))
lista = []
for i in matriz_base:
    matrix = []
    for j in i:
        matrix.append(j*fator)
    lista.append(matrix)
print(lista)