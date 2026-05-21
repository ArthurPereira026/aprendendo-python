ano = int(input("Digite seu ano de nascimento aq: "))
resultado = 2026 - ano

if resultado <=17 :
    print("Menor de Idade")
elif resultado <=59 :
    print("Adulto")
else:
    print("Idoso")
