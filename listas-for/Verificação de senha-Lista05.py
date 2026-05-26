senha = 12345678

for i in range(3):
    acesso = float(input("Digite sua senha aqui: "))

    if acesso == senha:
        print("Acesso permitido")
        break
    else:
        print("Senha Incorreta, Tente novamente")
else:
    print("Conta Bloqueada")
