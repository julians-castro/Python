print("Di la cantidad de notas a calcular")
n1 = int(input())
suma = 0
for i in range (n1):
    i = i + 1
    print("Ingrese la nota", i)
    nota = float(input())
    suma = suma + nota

prom = suma / i

if prom > 5: 
    print("Vuelva a ingresar los valores. Promedio no valido dentro del rango(0.0 a 5.0)")
elif prom < 3:
    print(f"Desaprobó con {prom}")
elif prom >= 3:
    print(f"Aprobó con {prom}")
       


