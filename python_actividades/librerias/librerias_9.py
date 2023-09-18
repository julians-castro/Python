import numpy as np

n = int(input("Ingresa el número de votos: "))

votos = np.zeros(4, dtype=int)  # Candidatos: 0, 1, 2, 3 correspondientes a blanco, candidato 1, candidato 2, candidato 3

for i in range(n):
    voto = int(input(f"Voto {i+1}: "))
    if voto >= 0 and voto <= 3:
        votos[voto] += 1
    else:
        print("Voto nulo.")

# Mostrar resultados
print("Total de votos para cada candidato:")
for i in range(1, 4):
    print(f"Candidato {i}: {votos[i]} votos")

print(f"Votos en blanco: {votos[0]}")
votos_nulos = n - sum(votos)
print(f"Votos nulos: {votos_nulos}")
