numero = []


for i in range(6):
    numeros = float(input(f"Digite o {i+1}° primeiro número: ").replace(",","."))
    numero.append(numeros)
numero.sort()

print(numero)
print(f"O maior número é:", max(numero))
print(f"O menor número é:", min(numero))

soma = sum(numero)
print(soma)

