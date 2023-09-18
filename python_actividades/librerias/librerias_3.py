import numpy as np

numero_decimal = int(input("Ingresa un número entero decimal: "))

digitos_binarios = []
while numero_decimal > 0:
    residuo = numero_decimal % 2
    digitos_binarios.insert(0, residuo)
    numero_decimal //= 2

digitos_binarios_array = np.array(digitos_binarios)

print("Dígitos binarios:", digitos_binarios_array)
