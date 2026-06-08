estoque = [[12, 5, 8],
            [3, 15, 2],
            [19, 0, 7]]

prateleira,divisoria = input("Fale em qual prateleira e divisória você gostaria de verificar separado por virgula: ").split(",")
prateleira = int(prateleira)-1
divisoria = int(divisoria)-1

print(estoque[prateleira][divisoria])