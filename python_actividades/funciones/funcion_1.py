l=[]
for i in range(1,4):
    n2 = int(input("Dame los numeros"))
    l.append(n2)
l.sort(reverse=True)
print(f"El maximo de los tres numeros es: {l[0]}")
