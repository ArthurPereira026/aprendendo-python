matriz_quadrada = [    [5, 2, 9],
                       [1, 8, 3],
                       [4, 7, 6]]
soma = 0
numeros = []
for i in range(len(matriz_quadrada)):
    numeros.append(str(matriz_quadrada[i][i]))
    soma += matriz_quadrada[i][i]
print(f"a soma da diagonal da matriz {"+".join(numeros)} = {soma}")