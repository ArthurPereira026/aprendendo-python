frequencia = int(input("Digite a frenquencia do aluno: "))

if frequencia > 0:
    nota1 = float(input("Digite aqui a nota: ").replace("," , "."))
    nota2 = float(input("Digite aqui a nota: ").replace("," , "."))

    media = float(nota1 + nota2)/2

    if media >= 7:
        print("aprovado")
    elif media >= 5:
        print("Recuperação")
        pvrec = float(input("Digite a nota da Prova de recuperação: ").replace("," , "."))
        if pvrec >= 5:
            print("Aprovado via prova de recuperação")
        else:
            print("Vai para a prova final")
            pvfinal = float(input("Digite aq a nota da prova final: ").replace("," , "."))
            if pvfinal >= 6:
                print("Você passou pela prova final")
            else:
                print("Reprovado")
else:
    print("Aluno nunca veio a aula")  
