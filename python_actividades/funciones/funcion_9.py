def elementos_unicos(lista):
    lista_unica = []
    for elemento in lista:
        if elemento not in lista_unica:
            lista_unica.append(elemento)
    return lista_unica
print(elementos_unicos(lista=[5,9,8,7,4]))