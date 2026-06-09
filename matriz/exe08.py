buscador = [[10, 50, 40],
           [25, 67, 35],
           [78, 89, 34]]

busca = int(input("Digite o número que deseja procurar: "))
achou = False

for i in range(len(buscador)):
    for j in range(len(buscador)):
        if buscador[i][j] == busca:
            print(f"O número que você procura está na linha {i+1} e na coluna {j+1}")
            achou = True
            break
    if achou:
        break

if not achou:
    print("O seu número n está nessa lista")
