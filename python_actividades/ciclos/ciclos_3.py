n1 = int(input("Cuantos terminos de la sucesion fibonacci quieres ver: "))
termino1 = 0
termino2 = 1
for i in range (1,n1+1):
    r = termino1 + termino2
    termino1 = termino2
    termino2 = r
    print(termino2)