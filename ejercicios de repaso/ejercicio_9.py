import random
M = int(input("ingrese cantidad de columnas: "))
N = int(input("ingrese cantidad de filas: "))
m = [[random.randint(1,1000) for j in range(M)] for i in range(N)]

for f in m:
    print(f)