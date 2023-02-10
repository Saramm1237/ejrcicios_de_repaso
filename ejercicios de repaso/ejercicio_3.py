import random
n = int(input("ingrese cuantos numeros aleatorios quiere obtener"))
aleatorios = [random.randint(0,1000) for _ in range(n)]
print(aleatorios)