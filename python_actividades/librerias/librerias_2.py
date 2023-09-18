import sympy

numero = int(input("Ingresa un número entero: "))

es_primo = sympy.isprime(numero)

if es_primo:
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")

