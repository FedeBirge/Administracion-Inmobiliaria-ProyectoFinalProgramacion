
from os import system

class tipo:
    Nombre = ""

    def __init__(self, nombre=''):
        self.Nombre = nombre

    def getNombre(self):
        return self.Nombre

    def setNombre(self, nombre):
        self.Nombre = nombre

    def __str__(self):
        return str(self.Nombre)

   
if __name__ == "__main__":
    print("Modulo de la clase tipo")
