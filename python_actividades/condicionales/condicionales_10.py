print("Dime cuantas llantas vas a comprar")
n1 = int(input())
if n1 == 0 and n1 < 6:
     valor_llanta = 240000 * n1
     print(f"El valor a pagar es de {valor_llanta}")
elif n1 == 6 or n1 == 7:
     valor_llanta = 221000 * n1
     print(f"El valor a pagar es de {valor_llanta}")
elif n1 > 7:
     valor_llanta = 180000 * n1
     print(f"El valor a pagar es de {valor_llanta}") 
            