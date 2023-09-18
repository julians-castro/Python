l=[]
n1 = int(input("Dame la cantidad de numeros para saber cual es el mas pequeño: "))
for i in range(1,n1+1):
    n2 = int(input("Dame los numeros: " ))
    l.append(n2)
l.sort()
print(f"El numero más pequeño es: {l[0]}")