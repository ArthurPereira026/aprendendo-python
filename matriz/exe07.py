matriz_A = [[1, 2, 3],
            [4, 5, 6]]

matrizT = [list(coluna) for coluna in zip(*matriz_A)]

for i in matrizT:
    print(i)

for i,valor in enumerate(matrizT,1):
    print(i,valor)
