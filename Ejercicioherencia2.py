class Animal():
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        print(f"Mi nombre es {self.nombre} y mi especie {self.especie}")

class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        self.raza = raza
        print(f"Mi raza es {self.raza}")


Axel = Perro("Axel", "Perro", "Schnauzer")