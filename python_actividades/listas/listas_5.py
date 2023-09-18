num_elementos = int(input("Numero lista: "))
l = []
for i in range(0,num_elementos):
    elemento = str(input("Digite la palabra de la lista: "))
    l.append(elemento)

l.sort(key=len, reverse=True)
print(f"La palabra más larga es: {l}")