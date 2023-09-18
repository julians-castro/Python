def factoria():
    n1 = int(input("Dime a que numero quieres sacarle factorial: "))
    resultado = 1
    for i in range(1,n1+1):
        resultado = resultado*i
    return resultado    
print(factoria())