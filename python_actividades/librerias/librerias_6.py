import numpy as np

n = int(input("Ingresa el número de lanzamientos a simular: "))

lanzamientos = np.random.randint(1, 7, size=n)

contador_tres = np.count_nonzero(lanzamientos == 3)

print(f"En {n} lanzamientos, se obtuvo el número 3 un total de {contador_tres} veces.")
