listaPrincipal = []
listaPares = []
listaImpares = []

for i in range(10):
    numero = int(input(f"Digite o seu {i+1}° aqui: ").replace(",","."))
    listaPrincipal.append(numero)

for x in listaPrincipal:
    resto = x % 2

    if resto == 0:
        listaPares.append(x)
    else:
        listaImpares.append(x)

print(f"Lista Principal {listaPrincipal}" )
print(f"Lista de pares {listaPares}")
print(f"Lista de impares {listaImpares}")