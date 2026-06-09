vendas = [[1200, 850, 900, 1500],
          [900, 1100, 1000, 1300],
          [1500, 1600, 1400, 1800],
          [700, 600, 800, 900]]

vendas_vendedores = []
vendas_por_dia = [0, 0, 0, 0]
for vendedores in vendas:
    totalVendas = 0
    for valorDias in vendedores:
        totalVendas += valorDias
    vendas_vendedores.append(totalVendas)


for vendedor in range(len(vendas)):
    for dia in range(len(vendas[0])):
        vendas_por_dia[dia] += vendas[vendedor][dia]

print("O total de vendas por  vendedor foi de: ")
for i in range(len(vendas)):
    print(f"Vendedor {i+1} = R$ {vendas_vendedores[i]:.2f}")

print(" ")

print("O total de vendas por dia foi de: ")
for i in range(len(vendas)):
    print(f"Dia {i+1} = R$ {vendas_por_dia[i]:.2f}")