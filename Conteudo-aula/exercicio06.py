lado1 = float(input("Digite sua medida aq; ").replace("," , "."))
lado2 = float(input("Digite sua segunda medida aq: ").replace("," , "."))
lado3 = float(input("Digite sua terceira medida aq: ").replace("," , "."))

if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1 :
    print("Isto n é possivel")
else:
    if lado1 == lado2 == lado3:
        print("Isto é um triângulo Equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Isto é um triângulo Isósceles")
    elif lado1 != lado2 != lado3:
        print("Isto é um triângulo Escaleno")
