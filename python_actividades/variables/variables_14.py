n1 = int(input("Dame la distancia en metros a transformar: "))
print("Selecciona el numero dependiendo a lo que quieras convertir")
print("1.km 2.cm 3.mm")
n2 = int(input())
if n2 == 1:
    resultado = n1/1000
    print(f"Dan {resultado} km")
elif n2 == 2:
    resultado = n1*100
    print(f"Dan {resultado} cm")
elif n2 == 3:
    resultado = n1*1000
    print(f"Dan {resultado} mm")
elif n2 > 3:
    print("Error, reinicia maldita puta")
elif n2 <= 0:
    print("error, reinicia maldita puta")