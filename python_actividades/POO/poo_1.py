class Rectangle:
    def __init__(self, longitud: float, anchura: float ):
        self.longitud = longitud
        self.anchura = anchura 

    def area_rectangulo(self):
         resultado = 1
         resultado = self.longitud * self.anchura
         return resultado
n1 = float(input("Dime la longitud de tu verga: "))
n2 = float(input("Dime la anchura de su verga: "))
resultado1 = Rectangle(n1,n2)
print(resultado1.area_rectangulo())