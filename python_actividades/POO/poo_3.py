class resultado:
    def __init__(self,base: float, exponente: float):
        self.base = base
        self.exponente = exponente

    def resultadonum(self):
        return pow(self.base, self.exponente)
n1 = float(input("Dime la base: "))
n2 = float(input("Dime el exponente: "))
exponente = resultado(n1,n2)
print(exponente.resultadonum())