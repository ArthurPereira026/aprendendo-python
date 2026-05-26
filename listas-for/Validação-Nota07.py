numero = int(input("Digite um Numero : "))

while numero < 0 or numero > 10:
    numero = int(input("Digite Novamente, Numero invalido: "))
else:
    print(f"Número valido: {numero}")