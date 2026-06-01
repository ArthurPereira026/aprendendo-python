vendas = [1200.50, 3400.00, 980.00, 5600.20, 2100.00, 850.00]
maiorVendas = []

for i in vendas:
    media = sum(vendas) / len(vendas)
    if i > media:
        maiorVendas.append(i)

print(maiorVendas)

