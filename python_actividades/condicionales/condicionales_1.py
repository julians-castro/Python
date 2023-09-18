print("Dame un numero para determinar si es par, impar o cero")
n1 = int(input(""))
if n1 == 0:
    print("El numero es cero")  
elif n1%2 == 0:
    print("El numero es par")
elif n1%2 != 0:
    print("El numero es impar")
      