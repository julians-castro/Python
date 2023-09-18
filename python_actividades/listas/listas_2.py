def multiplicacion(lista: list):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion


l = [1, 2, 3, 4, 5]
resultado = multiplicacion(l)
print("La multiplicación es:", resultado)