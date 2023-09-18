def palindromo(cadena):
    
    cadena = cadena.lower().replace(" ", "")

    
    for i in range(len(cadena) // 2):
        if cadena[i] != cadena[-1 - i]:
            return False
    return True

cadena1 = "Ana"
cadena2 = "Anita lava la tina"
cadena3 = "Hola mundo"

print(palindromo(cadena1))  
print(palindromo(cadena2))   
print(palindromo(cadena3)) 