print("Dime tu peso en kilogramos")
n1 = float(input())
print("Dime tu estatura en metros ejemplo: 1.82")
n2 = float(input())
imc = n1 / (n2*n2)
if imc < 18.5:
    print(f"Estás en desnutrición con un indice de {imc} IMC")
elif imc >= 18.5 and imc < 25:
    print(f"Estás normal con un indice de {imc} IMC")
elif imc >= 25 and imc < 30:
    print(f"Estás en sobrepeso con un indice de {imc} IMC") 
elif imc >= 30 and imc < 35:
    print(f"Estás en obesidad tipo 1 con un indice de {imc} IMC")       
elif imc >= 35 and imc < 40:
    print(f"Estás en obesidad tipo 2 con un indice de {imc} IMC")
elif imc >=40:
    print(f"Estás en obesidad tipo 3 con un indice de {imc} IMC")    