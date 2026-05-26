email = ["joao@gmail.com", "maria@senac.df", "pedro@outlook.com", "ana@senac.df"]
listaSenac = []

for i in email:
    if i.endswith("@senac.df"):
        listaSenac.append(i)

print(listaSenac)