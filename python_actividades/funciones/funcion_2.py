def cuadrado(l: float):
    return l ** 2

def rectangulo(l1: float, l2: float):
    return l1 * l2

def triangulo(b: float, h: float):
    return b * h / 2

def circulo(r: float, pi = 3.1415):
    return pi * r ** 2

def rombo(d1: float, d2: float):
    return d1 * d2 / 2

def trapecio(b1: float, b2: float, h: float):
    return (b1 + b2) / 2 * h

l: str = input("Coloque la letra que corresponda a la figura para encontrar su área:\na. Cuadrado\nb. Rectángulo\nc. Triángulo\nd. Círculo\ne. Rombo\nf. Trapecio\n -> ")
area = 0
error = False

if l == "a":
    n1 = float(input("Coloque el valor de un lado del cuadrado: "))
    area = cuadrado(n1)
elif l == "b":
    n1 = float(input("Coloque el valor del lado mayor del rectángulo: "))
    n2 = float(input("Coloque el valor del lado menor del rectángulo: "))
    area = rectangulo(n1, n2)
elif l == "c":
    n1 = float(input("Coloque el valor de la base del triángulo: "))
    n2 = float(input("Coloque el valor de la altura del triángulo: "))
    area = triangulo(n1, n2)
elif l == "d":
    n1 = float(input("Coloque el valor del radio del círculo: "))
    area = circulo(n1)
elif l == "e":
    n1 = float(input("Coloque el valor de la diagonal menor del rombo: "))
    n2 = float(input("Coloque el valor de la diagonal mayor del rombo: "))
    area = rombo(n1, n2)
elif l == "f":
    n1 = float(input("Coloque el valor de la base menor del trapecio: "))
    n2 = float(input("Coloque el valor de la base mayor del trapecio: "))
    n3 = float(input("Coloque el valor de la altura del trapecio: "))
    area = trapecio(n1, n2, n3)
else:
    error = True

if error == False:
    print(f"El área tiene un valor de {area}")
else:
    print("Coloque una letra correcta")