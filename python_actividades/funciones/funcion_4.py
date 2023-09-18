def multiplicacion(l1: list[float]):
    resultado = 1
    for i in range(len(l1)):
        resultado *= l1[i]
    return resultado

l = [8,2,3,-1,7]
print(multiplicacion(l))