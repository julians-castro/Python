print("Dime el valor de la cuenta")
n1 = int(input())
if n1 < 150000:
    print("Solo puedes pagar en efectivo")
elif n1 >= 150000 and n1 < 300000:
    print("Solo puedes pagar con celular")
elif n1 >=300000 and n1 <= 600000:
    print("Solo puedes pagar con tarjeta de debito")
elif n1 > 600000:
    print("Solo puedes pagar con tarjeta de credito")            