print("Dime tu genero")
print("1.Femenino 2.Masculino")
n1 = int(input())
print("Dime tu edad en años")
n2 = int(input())
if n1 == 1:
    pulsaciones = (220-n2)/10
    print(f"El numero de pulsaciones es {pulsaciones}")
elif n1 == 2:
    pulsaciones = (210-n2)/10
    print(f"El numero de pulsaciones es {pulsaciones}")
else: print("Error, numero ingresado no es correcto")    
        