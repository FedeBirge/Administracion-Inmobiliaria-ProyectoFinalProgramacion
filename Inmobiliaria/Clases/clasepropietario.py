
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

    # Metodo para insertar un propietario
    def insertarPropietario(self, propie):
        cone = conexion()
        if cone.conectado():
            try:

                propie.setNombre(
                    input("Ingrese el nombre completo del propietario: "))
                print()
                propie.setDireccion(propie.getDireccion())
                propie.setDireccion(
                    input("Ingrese la dirección del propietario: "))
                print()
                propie.setContacto(propie.getContacto())
                propie.setContacto(
                    int(input("Ingrese el número de contacto del propietario: ")))
                print()
                cursor = cone.conexion.cursor()
                insertarPropietario = "INSERT INTO Propietario (Nombre, Direccion, Contacto) VALUES ('{}', '{}', '{}')".format(
                    propie.getNombre(), propie.getDireccion(), propie.getContacto())
                cursor.execute(insertarPropietario)
                cone.conexion.commit()
                print(cursor.rowcount, "PROPIETARIO REGISTRADO CON EXITO.")
            except Exception as e:
                print("Error al insertar el propietario: ", e)

    # Metodo interno para recuperar el ultimo id de la tabla propietario
    def RecuperarUltimoIdPropietario(self):
        cone = conexion()
        if cone.conectado():
            try:
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT MAX(Id_Propietario) FROM Propietario;")
                return int(cursor.fetchone()[0])
            except Exception as e:
                print("Error al recuperar el id del propietario: ", e)

    # Metodo para mostrar los datos del propietario de un id dado
    def MostrarPropietario(self, id):
        cone = conexion()
        if cone.conectado():
            try:
                cursor = cone.conexion.cursor()
                cursor.execute(
                    "SELECT * FROM Propietario WHERE Id_Propietario = {}".format(id))
                resultado = cursor.fetchall()
                print(tabulate(resultado, headers=[
                    "Id_Propietario", "Nombre", "Direccion", "Contacto"], tablefmt="fancy_outline"))
            except Exception as e:
                print("Error al mostrar el propietario: ", e)

    # Metodo para modificar los datos del propietario
    def modificarPropietario(self, id):
        cone = conexion()
        if cone.conectado():
            try:
                propie = propietario()
                if cone.conectado():
                    cursor = cone.conexion.cursor()
                    propie.setNombre(
                        input("Ingrese el nuevo nombre del propietario: "))
                    print()
                    propie.setDireccion(propie.getDireccion())
                    propie.setDireccion(
                        input("Ingrese la nueva dirección del propietario: "))
                    print()
                    propie.setContacto(propie.getContacto())
                    propie.setContacto(
                        int(input("Ingrese el nuevo número de contacto del propietario: ")))
                    print()
                    modificar = "UPDATE Propietario SET Nombre = '{}', Direccion = '{}', Contacto = '{}' WHERE Id_Propietario = {}".format(
                        propie.getNombre(), propie.getDireccion(), propie.getContacto(), id)
                    cursor.execute(modificar)
                    cone.conexion.commit()
                    print(cursor.rowcount, "PROPIETARIO MODIFICADO CON EXITO.")
            except Exception as e:
                print("Error al modificar el propietario: ", e)
        

if __name__ == '__main__':
    print("Soy la Clase Propietario")
