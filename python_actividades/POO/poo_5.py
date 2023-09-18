import random
class Ave:
    def __init__(self, nombre, color, habitat):
        self.nombre = nombre
        self.color = color
        self.habitat = habitat

    def volar(self):
        print(f"{self.nombre} está volando.")

    def cantar(self):
        print(f"{self.nombre} está cantando.")

class Aguila(Ave):
    def __init__(self, nombre, color, habitat, envergadura):
        super().__init__(nombre, color, habitat)
        self.envergadura = envergadura

    def cazar(self):
        print(f"{self.nombre} está cazando en el aire.")

class Buho(Ave):
    def __init__(self, nombre, color, habitat, tipo_vuelo):
        super().__init__(nombre, color, habitat)
        self.vuelo = tipo_vuelo

    def buscando_presa(self):
        print(f"{self.nombre} está girando 270 grados su cuello hacia la derecha e izquierda buscando una presa.")
    
    def cantar(self):
        print(f"{self.nombre} está cantando con un tono grave: 'Ho-ho-ho'.")
    
    def cazandoconejos(self):
    
        print("¡Eres un conejo siendo cazado por un Buho!")
        print("Elige tu camino:")
        print("1. Camino 1")
        print("2. Camino 2")
        
        eleccion = int(input("Ingresa el número de tu elección: "))
        
        aux = 0
        for i in range(1,21):
            num_random = random.randint(1,5)
            print(f"Elige tu camino: (Vas en la elección {i} de 10)")
            print("1. Camino 1")
            print("2. Camino 2")
            print("3. Camino 3")
            print("4. Camino 4") 
            print("5. Camino 5")  
            eleccion = int(input("Ingresa el número de tu elección: "))           
            if eleccion <= 0 or eleccion >= 6:
                print("numero no valido, se reinicia la caza")
                break
            elif eleccion == num_random:
                print("Te cazo el buho")
                break
            else:
                print("Te salvaste del buho") 



aguila_real = Aguila("Águila Real", "marrón", "montañas", 2.1)
Buho_2 = Buho("Buho Real", "pardo", "Europa, Asia y Partes de africa", "Silencioso")

aguila_real.volar()
Buho_2.cantar()
aguila_real.cazar()
Buho_2.buscando_presa()
Buho_2.cazandoconejos()
