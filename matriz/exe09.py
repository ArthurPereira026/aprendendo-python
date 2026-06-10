notas = [[7.0, 8.5, 6.0, 7.5],
         [9.0, 9.5, 10.0, 8.5],
         [5.0, 6.0, 5.5, 4.0]]

somaNotas = [sum(n)for n in notas]
mediaFinal = []

for media in somaNotas:
    media = media/4
    mediaFinal.append(media)

print(mediaFinal)