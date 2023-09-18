import random

# Generar un número entero al azar entre 1 y 100
numero_secreto = random.randint(1, 100)

print("Bienvenido al juego de adivinar el número.")
print("Estoy pensando en un número entre 1 y 100.")
print("Puedes ingresar tus suposiciones. Te diré si estás cerca o lejos del número.")

intentos = 0
suposicion = None

while suposicion != numero_secreto:
    suposicion = int(input("Ingresa tu suposición: "))
    intentos += 1

    if suposicion < numero_secreto:
        print("Más alto...")
    elif suposicion > numero_secreto:
        print("Más bajo...")

print(f"Adivinaste el número {numero_secreto} en {intentos} intentos.")

