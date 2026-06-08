print("*********************************************")
print("  Bem Vindo ao campo de Batalha Naval 4 x 4")
print("*********************************************")

print("""
        [['~','~','~','~'],
         ['~','~','~','~'],
         ['~','~','~','~'],
         ['~','~','~','~']]
""")

oceano = [['~','~','~','~'],
          ['~','~','~','~'],
          ['~','~','~','~'],
          ['~','~','N','~']]

while True:
    linha,coluna = input("Mire ultilizando a linha e a coluna separando por virgula: ").split(",")
    linha = int(linha)-1
    coluna = int(coluna)-1
    if linha and coluna == 'N':
        print("Você Afundou o Navio")
        break
    else:
        linha, coluna = input("Ops voçê errou, Que tal tentar novamente: ").split(",")
