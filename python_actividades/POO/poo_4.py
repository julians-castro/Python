class Vehiculo:
    def __int__(self, marca: str, placa: str, modelo: str, color: str, tipo_vehiculo: str, espacio_aparcado: int, tiempo_reserva: int, dia_ingreso: int, hora_ingreso: int):
        self.marca = marca
        self.placa = placa
        self.modelo = modelo
        self.color = color
        self.tipo_vehiculo = tipo_vehiculo
        self.espacio_aparcado = espacio_aparcado
        self.tiempo_reserva = tiempo_reserva
        self.dia_ingreso = dia_ingreso
        self.hora_ingreso = hora_ingreso

    def obtener_placa(self):
        self.placa = input("Dime los numeros de la placa: ")
        
    def obtener_diaingreso(self):
        self.dia_ingreso = input("Dime el dia que ingreso el carro: ")
            
    def verificar_placa(self):
        uno_cinco = ["1","2","3","4","5"]
        seis_cero = ["6","7","8","9","0"]
        auxpico = int() 
        self.placa = self.placa[5]       
        for i in range(5):
            if self.placa == seis_cero[i] and int(self.dia_ingreso) % 2 == 0 or self.placa == uno_cinco[i] and int(self.dia_ingreso) % 2 != 0:
                auxpico = 0
                break
            else:
                auxpico = 1
        if auxpico == 1:
            print("Tenes pico y placa")
        elif auxpico == 0:
            print("No tenes pico y placa")    
carrito1 = Vehiculo()
carrito1.obtener_placa()
carrito1.obtener_diaingreso()
carrito1.verificar_placa()