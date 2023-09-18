print("¿Cual es tu nombre?")
nombre = input()
print("Dime tu edad")
edad = int(input())
if edad > 100:
    print(f"{nombre} ingresa una edad válida")
elif edad <=0:
    print(f"{nombre} ingresa una edad válida") 
elif edad >= 18:
    print(f"{nombre} usted es mayor de edad")
elif edad < 18:
    print(f"{nombre} usted es menor de edad")           