resultado = []

while True:

    n1 = int(input("Digite o primeiro número da soma: "))
    n2 = int(input("Digite o segundo número da soma: "))
    soma = n1 + n2
    resultado.append(soma)
    if n1 or n2 == 0 :
        break

print(resultado)