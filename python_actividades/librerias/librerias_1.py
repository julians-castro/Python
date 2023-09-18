import numpy as np

entrada = input("Ingresa los valores separados por espacios: ")
valores = np.array([float(valor) for valor in entrada.split()])

mayor = np.max(valores)

print("El mayor valor es:", mayor)
