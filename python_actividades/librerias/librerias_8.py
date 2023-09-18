import numpy as np
import matplotlib.pyplot as plt

numeros = np.random.randint(1, 21, size=10)


for i, numero in enumerate(numeros, start=1):
    print(f"Número {i}: {'*' * numero}")

plt.bar(range(1, 11), numeros)
plt.xlabel('Número')
plt.ylabel('Valor')
plt.title('Representación')
plt.show()
