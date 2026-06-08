inicial = int(input("Digite em qual número deve começar: "))
final = int(input("Digite em qual número deve acabar: "))
passo = int(input("Digite de quanto em quanto deve andar: "))
saida = []

for i in range(inicial,final,passo):
    saida.append(i)

print(saida)
