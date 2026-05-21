salario = float(input("Digite seu salário bruto aqui: ").replace("," , "."))
parcela = float(input("Digite o valor da parcela de empréstimo aq: ").replace("," , "."))

valorMaxParcela  = salario*0.3

if parcela > valorMaxParcela:
    print("Seu empréstimo foi negado")
else:
    print(f"Seu empréstimo {parcela:.0f} de foi aprovado com sucesso")

