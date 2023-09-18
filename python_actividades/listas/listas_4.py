def eliminar(lista: list):
    lista0 = []
    for i in lista:
        if i not in lista0:
            lista0.append(i)
    return lista0

lista1 = [1, 2, 2, 3, 4, 4, 5, 6, 6]
lista0 = eliminar(lista1)
print(f"Lista original: {lista1}")
print(f"Lista sin duplicados: {lista0}")
