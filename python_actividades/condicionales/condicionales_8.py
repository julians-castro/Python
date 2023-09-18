a = int(input("Ingresa un numero: "))

b = int(input("Ingresa otro numero:"))

c = int(input("Ingresa otro numero: "))

if a != b and a != c and b != c:
    if a < b:
        if a < c:
            if (b < c):
                print(a,b,c)
                print(c,b,a)
            else:
                print(a,c,b)
                print(b,c,a)
        else:
            print(c,a,b)
            print(b,a,c)
    else:
        if b < c:
            if c < a:
                print(b,c,a)
                print(a,c,b)
            else:
                print(b,a,c)
                print(c,a,b)
        else:
            print(c,b,a)
            print(a,b,c)
else:
    print("Los numeros deben ser diferentes: ")