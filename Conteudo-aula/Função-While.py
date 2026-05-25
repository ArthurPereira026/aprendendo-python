listaIdades = []
continuar = input("Quer começar o questionário? (s/n)").upper()[0]

while continuar == "S" or continuar == "C":
        idade = int(input("Digite sua idade: "))
        listaIdades.append(idade)
        continuar = input("Quer continuar (s/n)").upper()[0]
listaIdades.sort()

print(listaIdades)