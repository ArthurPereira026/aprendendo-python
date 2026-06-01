maiorDe18 = []
listaHomens = []
femininoMenor20 = []
continuar = "S"

while continuar == "S":
    idade = int(input("Digite sua idade: "))
    sexo = input("Qual é seu gênero?(M/F) ").upper()[0]

    if idade > 18:
        maiorDe18.append(idade)
    if sexo == "M":
        listaHomens.append(sexo)
    if sexo  == "F" and idade < 20:
        femininoMenor20.append(sexo + str(idade))

    continuar = input("Deseja continuar os cadastros?: ").upper()[0]

print(f"Essa é a quantidade de cadastrados com mais de 18 anos: {len(maiorDe18)}")
print(f"Esse foi o total de pessoas cadastradas do gênero masculino: {len(listaHomens)}")
print(f"Essa é a quantidade de pessoas do gênero feminino e menores de 20 anos cadastradas: {len(femininoMenor20)}")
