turma = [ ["Ana", 8.0, 9.0], ["Pedro", 5.5, 6.0], ["Carlos", 7.5, 7.0] ]
mediaTurma = []

for i in turma:
    media = (i[1]+i[2])/2
    lista = [i[0],media]
    mediaTurma.append(lista)

print(f"A média da turma foi {mediaTurma}")