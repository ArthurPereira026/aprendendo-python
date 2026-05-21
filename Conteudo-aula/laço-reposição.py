#Simulando uma chamada

alunos = ["Jaqueline", "Débora", "Evilyn", "Arthur", "Izaac", "Escobar","Rafael", "Luã", "Lindoso", "Wojcieskovsky"]

alunos.sort()

print(f"Quantos alunos tem na sala: {len(alunos)}")

print(f"--- Iniciando a chamada! ---")
for i in alunos:
    print(f"Alunos(a) {i} está presente!")
print("--- Fim da chamada! ---")