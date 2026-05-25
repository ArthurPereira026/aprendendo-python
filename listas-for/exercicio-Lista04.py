listaIdades = []
listaMaior = []
listaMenor = []
continuar = input("Podemos começar a Intrevista? (s/n): ").upper()[0]

while continuar == "S" or continuar == "C":
    ano = int(input(f"Digite o seu ano de nascimento aq: "))
    listaIdades.append(ano)
    listaIdades.sort()
    continuar = input("Deseja continuar? (s/n): ").upper()[0]

for x in listaIdades:
    calculo = 2026 - x

    if calculo <= 17:
        listaMenor.append(calculo)
    else:
        listaMaior.append(calculo)

print(f"Lista de anos dos intrevistados {listaIdades} Quantidade de intrevistados:{len(listaIdades)} ")
print(f"Idade dos anos de Maior idade {listaMaior} quantidade de Maior Idade: {len(listaMaior)}")
print(f"Idade dos anos menores de Idade {listaMenor} Quantidade de Menor idade: {len(listaMenor)}")