class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Mi nombre es {self.nombre} y mi edad es {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        print(f"Mi grado es {self.grado}")

Maicol = Estudiante("Maicol", 22, "Septimo grado")
