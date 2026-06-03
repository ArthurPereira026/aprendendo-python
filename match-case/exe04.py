while True:
    mes = input("Digite um mês do ano para saber sua estação do ano: ").lower()
    match mes:
        case "janeiro" |"fevereiro"|"dezembro":
            print(f"A estação do {mes} é verão")
        case "setembro"|"outubro"|"novembro":
            print(f"A estação do {mes} é Primavera")
        case "junho"|"julho"|"agosto":
            print(f"A estação do {mes} é Inverno")
        case "março"|"abril"|"maio":
            print(f"A estação do {mes} é Outono")
        case _:
            print("Digite um mês valido")
