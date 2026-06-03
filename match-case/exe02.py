while True:
    nota = input("Digite sua nota baseada em letras de A a F onde A é ótimo e F Reprovado: ").upper()
    match nota:
        case "A":
            print("Excelente Trabalho!")
        case "B":
            print("Bom Desempenho")
        case "C":
            print("Satisfatório")
        case "D":
            print("Abaixo da Média (Atenção)")
        case "F":
            print("Reprovado")
        case _:
            print("Conceito desconhecido")
            break
