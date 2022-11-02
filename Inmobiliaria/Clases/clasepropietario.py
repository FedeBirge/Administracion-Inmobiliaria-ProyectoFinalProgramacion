
import sys
sys.path.append(r"..\\Inmobiliaria")
from Conexion.conexionbd import conexion  # importar la clase conexion
from tabulate import tabulate

class propietario: # Clase propietario 
    Nombre = ""
    Direccion = ""
    Contacto = 0

    def __init__(self, nombre='', direccion='', contacto=0):
        self.Nombre = nombre
        self.Direccion = direccion
        self.Contacto = contacto

    def getNombre(self):
        return self.Nombre

    def getDireccion(self):
        return self.Direccion

    def getContacto(self):
        return self.Contacto

    def setNombre(self, nombre):
        self.Nombre = nombre

    def setDireccion(self, direccion):
        self.Direccion = direccion

    def setContacto(self, contacto):
        self.Contacto = contacto

    def __str__(self):
        return "Nombre del propietario: " + str(self.Nombre) + " Direccion: " + str(self.Direccion) + "  Contacto: " + str(self.Contacto)


if __name__ == '__main__':
    print("Soy la Clase Propietario")
