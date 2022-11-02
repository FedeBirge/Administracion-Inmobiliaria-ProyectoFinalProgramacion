
from os import system
class operatoria:
    NombreOp = ""

    def __init__(self, nombre=''):
        self.NombreOp = nombre

    def getNombreOp(self):
        return self.NombreOp

    def setNombreOp(self, nombre):
        self.NombreOp = nombre

    def __str__(self):
        return str(self.NombreOp)

   
        
if __name__ == '__main__':
    print("Soy la Clase Operatoria")
