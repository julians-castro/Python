def suma(l1: list[float]):
    resultado = 0
    for i in range(len(l1)):
        resultado += l1[i]
    return resultado

l = [8,2,3,0,7]
print(suma(l))