matriz_valores = [
    [15, 42, 7],
    [23, 91, 12],
    [34, 8, 55]
]

matriz_S = [n for conjunto in matriz_valores for n in conjunto]
maior = max(matriz_S)
menor = min(matriz_S)

print(f"O seu maior número é {maior} e ele está na posição {matriz_S.index(maior)}, O menor número da sua matriz é: {menor} e está na posição {matriz_S.index(menor)}")