def suma(lista: list):
    suma = 0
    for i in lista:
        suma += i
    return suma


l = [1, 2, 3, 4, 5]
resultado = suma(l)
print("La suma es:", resultado)
