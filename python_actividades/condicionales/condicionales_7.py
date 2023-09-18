print("Dime la cantidad de la temperatura")
n1 = float(input())
print("Dime en que temperatura esta")
print("1.Kelvin 2.Celcius 3.Fahrenheit 4.Rankine 5.Reaumur")
n2 = int(input())
if n2 == 1:
    print("Dime a que temperatura quieres convertir") 
    print("1.Celcius 2.Fahrenheit 3.Rankine 4.Reaumur")
    kelvin = int(input())
    if kelvin == 1:
        resultado_kelvin = n1 - 273.15
        print(f"{n1} grados Kelvin en Celcius son: {resultado_kelvin}")
    elif kelvin == 2:
        resultado_kelvin = (n1)*9/5-459.67
        print(f"{n1} grados Kelvin en Fahrenheit son: {resultado_kelvin}")
    elif kelvin == 3:
        resultado_kelvin = (n1)*9/5
        print(f"{n1} grados Kelvin en Rankine son: {resultado_kelvin}")
    elif kelvin == 4:
        resultado_kelvin = (n1-273.15)*4/5
        print(f"{n1} grados Kelvin en Reaumur son: {resultado_kelvin}")
elif n2 == 2:
    print("Dime a que temperatura quieres convertir")
    print("1.Kelvin 2.Fahrenheit 3.Rankie 4.Reaumur")
    celcius = int(input())
    if celcius == 1:
        resultado_celsius = n1 + 273.15
        print(f"{n1} grados Celcius en Kelvin son: {resultado_celsius}")
    elif celcius == 2:
        resultado_celsius = (n1)*9/5+32
        print(f"{n1} grados Celcius en Fahrenheit son: {resultado_celsius}")
    elif celcius == 3:
        resultado_celsius = (n1 + 273.15)*9/5
        print(f"{n1} grados Celcius a Rankine son: {resultado_celsius}")
    elif celcius == 4:
        resultado_celsius = (n1)*4/5
        print(f"{n1} grados Celcius a Reaumur son: {resultado_celsius} ")
elif n2 == 3:
    print("Dime a que temperatura quieres convertir")
    print("1.Kelvin 2.Celcius 3.Rankine 4.Reaumur")
    fahrenheit = int(input())
    if fahrenheit == 1:
        resultado_fahrenheit = (n1+459.67)*5/9
        print(f"{n1} grados fahrenheit a Kelvin son: {resultado_fahrenheit}")
    elif fahrenheit == 2:
        resultado_fahrenheit = (n1-32)*5/9
        print(f"{n1} grados fahrenheit a Celcius son: {resultado_fahrenheit}")
    elif fahrenheit == 3:
        resultado_fahrenheit = n1+459.67
        print(f"{n1} grados fahrenheit a Rankine son: {resultado_fahrenheit}")
    elif fahrenheit == 4:
        resultado_fahrenheit = (n1-32)*4/9
        print(f"{n1} grados Fahrenheit a Reaumur son: {resultado_fahrenheit}")
elif n2 == 4:
    print("Dime a que temperatura quiere convertir")
    print("1.Kelvin 2.Celcius 3.Fahrenheit 4.Reaumur")
    rankine = int(input())
    if rankine == 1:
        resultado_rankine = (n1)*5/9
        print(f"{n1} grados Rankine a Kelvin son: {resultado_rankine}")
    elif rankine == 2:
        resultado_rankine = (n1 - 491.67)*5/9
        print (f"{n1} grados Rankine a Celcius son: {resultado_rankine}")
    elif rankine == 3:
        resultado_rankine = n1-459.67
        print(f"{n1} grados Rankine a Fahrenheit son: {resultado_rankine}")
    elif rankine == 4:
        resultado_rankine = (n1 - 491.67)* 4/9
        print(f"{n1} grados Rankine a Reaumur son: {resultado_rankine}")
elif n2 == 5:
    print("Dime a que temperaturas quieres convertir")
    print("1.Kelvin 2.Celcius 3.Fahrenheit 4.Rankine")
    reaumur = int(input())
    if reaumur == 1:
        resultado_reaumur = (n1)*5/4+273.15
        print(f"{n1} grados Reaumur a Kelvin son: {resultado_reaumur}")
    elif reaumur == 2:
        resultado_reaumur = (n1)*5/4
        print(f"{n1} grados Reaumur a Celcius son: {resultado_reaumur}")
    elif reaumur == 3:
        resultado_reaumur = (n1)*9/4+32
        print(f"{n1} grados Reaumur a Fahrenheit son: {resultado_reaumur}")
    elif reaumur == 4:
        resultado_reaumur = (n1)*9/4+491.67
        print(f"{n1} grados Reaumur a Rankine son: {resultado_reaumur}")



                                                       

