valor = int(input("Digite o valor que deseja sacar: "))
cedulas = [50,20,10,5,2]
i = 0

while valor > 0:
    quantidade = valor // cedulas[i]