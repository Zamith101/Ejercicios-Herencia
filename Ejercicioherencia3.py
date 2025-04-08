class Vehiculo():
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
        print(f"La marca del coche es {self.marca} y el año es {self.año}")

class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo = modelo
        print(f"el modelo del Vehiculo es {self.modelo}")

Carro = Coche("Lamborghini Aventador", 2025, "Huracán")