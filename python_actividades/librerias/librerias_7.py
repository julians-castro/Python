import numpy as np

contador_lanzamientos = 0

while True:
    lanzamiento = np.random.randint(1, 7)
    contador_lanzamientos += 1
    
    if lanzamiento == 5:
        break

print(f"Se necesitaron {contador_lanzamientos} lanzamientos para obtener el número 5.")
