print("Programa para calcular areas seleccione el número deacuerdo al area que desea encontrar")
print("1.Cuadrado 2.Rectángulo 3.Triángulo 4.Circulo 5.Rombo 6.Trapecio")
n1 = int(input())
if n1 <= 0:
    print("Reinicia el programa, número no valido")
elif n1 > 6:
    print("Reinicia el programa, número no valido")    
elif n1 == 1:
    print("Dime un lado del cuadrado")
    ladocuadrado = int(input())
    resultado_cuadrado = ladocuadrado * 2
    print(f"El area del cuadrado es: {resultado_cuadrado}")
elif n1 == 2:
    print("Dime la base del rectángulo")
    base_rectangulo = int(input())
    print("Dime la altura del rectángulo")
    altura_rectangulo = int(input())
    resultado_rectangulo = base_rectangulo * altura_rectangulo
    print(f"El area del rectángulo es: {resultado_rectangulo}")  
elif n1 == 3:
    def area(s,a,b,c):
        resultado = (s*(s-a)*(s-b)*(s-c))**0.5
        return resultado
    print("Dime el lado uno del triángulo")
    lado1_triangulo = int(input())
    print("Dime el lado dos del triángulo")
    lado2_triangulo = int(input())
    print("Dime el lado tres del triángulo")
    lado3_triangulo = int(input())
    perimetro_triangulo = lado1_triangulo + lado2_triangulo + lado3_triangulo
    semiperimetro_triangulo = perimetro_triangulo/2
    print("El area es:")
    print(area(semiperimetro_triangulo,lado1_triangulo,lado2_triangulo,lado3_triangulo)) 
elif n1 == 4:
    print("Dime el radio del circulo")
    radio_circulo = int(input())
    resultado_circulo = 3.14 * radio_circulo**2
    print(f"El area del circulo es{resultado_circulo}")
elif n1 == 5:
    print("Dime la diagonal mayor del rombo")
    diagonal_mayor = int(input())
    print("Dime la diagonal menor del rombo")
    diagonal_menor = int(input())
    resultado_rombo = (diagonal_mayor * diagonal_menor)/2
    print(f"El area del rombo es {resultado_rombo}")
elif n1 == 6:
    print("Dime la primera base")
    primera_base = int(input())
    print("Dime la segunda base")
    segunda_base = int(input())
    print("Dime la altura")
    altura_trapecio = int(input())
    resultado_trapecio = (primera_base + segunda_base)*altura_trapecio/2
    print(f"El area es {resultado_trapecio}")