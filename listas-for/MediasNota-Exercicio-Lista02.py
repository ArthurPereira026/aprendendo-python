listaNotas = []

for i in range(4):
    notas = float(input(f"Digite a {i+1}° nota: ").replace(",","."))
    listaNotas.append(notas)
media = sum(listaNotas)/len(listaNotas)

if media >= 7:
    print(*listaNotas,"parabéns vc foi Aprovado")
else:
    print("Infelizmente voçê foi Reprovado")


