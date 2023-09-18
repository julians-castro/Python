totalpp = int(input("dime el precio del producto: "))
cantp = int(input("dime la cantidad de producto: "))
totalpp = totalpp * cantp
iva = totalpp * 0.16
resultado = iva + totalpp
print(f"El precio es: {resultado}") 
