notasAlunos = [ ["joão", 8.7, 9.0],
                ["Maria", 7.3, 9.0],
                ["José", 8.3, 5.2] ]

mediaAlunos = []

for i in notasAlunos:
    media = (i[1]+i[2])/2
    lista = [i[0],media]
    mediaAlunos.append(lista)

print(f"lista de Notas dos alunos: {notasAlunos}")
print(f"Lista de médias dos alunos: {mediaAlunos}")