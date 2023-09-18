n1 = int(input("Dime el numero de la tabla de multiplicar, que quieras saber: "))
n2 = int(input("Dime hasta que numero quieres crear la tabla"))
for i in range (n2+1):
    multi = i * n1
    print(f"{n1} x {i} = {multi}")