idade = int(input("Digite sua idade aq: "))

if idade <= 9:
    print("Sua categoria é Mirim")
elif idade <=14:
    print("Sua categoria é infantil")
elif idade <= 19:
    print("Sua categoria é infanto")
elif idade <= 25:
    print("Sua categoria é Sub-21")
else:
    print("Sua categoria é Adulto/Master")