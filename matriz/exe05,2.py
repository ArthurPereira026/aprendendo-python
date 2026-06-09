vendas = [[1200, 850, 900, 1500],
          [900, 1100, 1000, 1300],
          [1500, 1600, 1400, 1800],
          [700, 600, 800, 900]]

vendasVendedores = [sum(vendedor) for vendedor in vendas]
vendasDias = [sum(dia)for dia in zip(*vendas)]

for i,valor in enumerate(vendasVendedores,1):
    print(f"O {i}° vendedor vendeu no total: R${valor}")

for i,valor in enumerate(vendasDias,1):
    print(f"O {i}° dia de vendas rendeu no total : R${valor}")