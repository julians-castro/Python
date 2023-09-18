import math
class Circulo:
    def __init__(self, radio: float, diametro: float):
        self.radio = radio
        self.diametro = diametro

    def area_circulo (self):
        resultado = math.pi * self.radio
        return resultado
    
    def perimetro_circulo (self):
        resultado = math.pi * self.diametro
        return resultado
msj =print("quieres saber el area o el perimetro del circulo presione 1 para area, 2 para perimeto")

msj = int(input(msj))
if msj == 1:
    n1 = float(input("Dime el radio del circulo: "))
    objeto1 = Circulo(n1,0)
    print(objeto1.area_circulo())
else:
    n1 = float(input("Dime el diametro del circulo: "))
    objeto1 = Circulo(0,n1)
    print(objeto1.perimetro_circulo())


