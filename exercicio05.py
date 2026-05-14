peso = float(input("Digite seu peso aqui: ").replace("," , "."))
altura = float(input("Digite sua altura aqui: ").replace("," , "."))

resultado = (altura**2)/peso

if resultado <= 18.4 :
    print("Você esta a baixo do Peso")
elif resultado <= 24.9:
    print("Seu peso está na Média Parabéns")
elif resultado <= 29.9 :
    print("Sobrepeso")
elif resultado <= 34.9 :
    print("Obesidade Grau I")
elif resultado <= 39.9 :
    print("Obesidade Grau II")
elif resultado >= 40:
    print("Obesidade Grau III")
else:
    print("Obito")