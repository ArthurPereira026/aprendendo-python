numero = float(input("Digite um número: ").replace("," , "."))
resultado = numero%2

if resultado == 0:
    print("Seu numero é par")
else:
    print("Seu número é ímpar")