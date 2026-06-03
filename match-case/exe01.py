while True:
    dia =  int(input("Digite um número de 1 a 7: "))
    match dia:
        case 1:
            print("Dia 1 é domingo")
        case 2:
            print("dia 2 é Segunda-Feira")
        case 3:
            print("Dia 3 é Terça-Feira")
        case 4:
            print("Dia 4 é Quarta-Feira")
        case 5:
            print("Dia 5 é Quinta-Feira")
        case 6:
            print("Dia 6 é Sexta-feira")
        case 7:
            print("Dia 7 é Sábado")
        case _:
            print("Dia invalido")
            break
