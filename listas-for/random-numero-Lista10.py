import random

numeroSorteado = random.randint(1, 20)
palpite = int(input("Faça um palpite de 1 a 20: "))


while palpite != numeroSorteado:

    if palpite > numeroSorteado:
        print("O Número que você digitou é maior que o número secreto")
    else:
        print("O Número que você digitou é menor que o número secreto")
    palpite = int(input("Tente Novamente: "))
print(f"Parabéns você acertou o número secreto que era: {numeroSorteado}")









            #elif palpite < numeroSorteado:
            #int(input("O Número que você digitou é menor que o número sorteado, Tente Novamente: "))
    #elif palpite == numeroSorteado:
        #print(f"Parabéns você acertou o número secreto que era: {numeroSorteado}")
        #break