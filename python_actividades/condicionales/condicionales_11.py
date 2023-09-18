print("Dime que que tamaño quieres la pizza")
print("1.pequeño 2.mediano 3.grande")
n1 = int(input())
print("Dime cuantos ingredientes adicionales quieres")
n2 = int(input())
n2 = n2*4000
if n1 == 1:
    precio_pizza = 15000 + n2
    print(f"El precio es {precio_pizza}")
elif n1 == 2:
    precio_pizza = 24000 + n2 
    print(f"El precio es {precio_pizza}")
elif n1 == 3:
    precio_pizza = 36000 + n2
    print(f"El precio es {precio_pizza}")        