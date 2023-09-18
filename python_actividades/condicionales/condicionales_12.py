print("Digite el valor de unidad del producto (sin punto, ni comas)")
n1 = int(input())
print("Digite la cantidad de producto a comprar")
n2 = int(input())
if n2 == 0 and n2 <= 5:
    precio_producto = n1 * n2 
    print(f"El precio es {precio_producto} y no aplica descuento")
elif n2 > 5 and n2 < 10:
    descuento = n1 * 0.05
    n1 = n1 - descuento
    precio_producto = n1 * n2
    print(f"El precio es {precio_producto}")
elif n2 >= 10:
    descuento = n1 * 0.08
    n1 = n1 - descuento
    precio_producto = n1 * n2
    print(f"El precio es {precio_producto}")  


