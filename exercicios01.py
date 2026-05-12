n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

resultado = n1 / n2
resultado2 = n1 % n2
resultado3 = n1 ** n2
print("resultado é: " , resultado)
print("o resultado2 é:" , resultado2)
print("o resultado3 é" , resultado3)

print("---------------------------------------------------------")
print("OPERADORES RELACIONAIS")
print("---------------------------------------------------------")


relação1 = n1 > n2
relação2 = n1 < n2
relação3 = n1 >= n2
relação4 = n1 <= n2
relação5 = n1 == n2
relação6 = n1 != n2

print("os resultados das relações estarao abaixo \n{} \n{} \n{} \n{} \n{} \n{}".format(relação1, relação2, relação3, relação4, relação5, relação6))
