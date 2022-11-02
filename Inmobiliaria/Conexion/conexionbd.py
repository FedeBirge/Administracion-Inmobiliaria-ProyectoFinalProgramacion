import mysql.connector
import time

class conexion: # Clase conexion
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',    # Ingrese su usuario AQUI si es diferente
                password='',    # Ingrese su password AQUI
                db='            # Ingrese el nobre de la base de datos AQUI
            )
        except mysql.connector.Error as err:
            print('Error al conectar a la Base de Datos')
            print(err)

    def getConection(self):
        return self.conexion

    def setConection(self, conexion):
        self.conexion = conexion

    def __str__(self):
        return "Conexion a la Base de Datos"

    def conectar(self): # Metodo para conectar la base de datos
        try:
            self.conexion.connect()
            if self.conexion.is_connected():
                print('Conexión exitosa ' +
                      time.strftime("%x") + '  ' + time.strftime("%X"))
        except mysql.connector.Error as err:
            print('Error al conectar a la Base de Datos')
            print(err)

    def desconectar(self): # Metodo para desconectar la base de datos   
        try:
            if self.conexion.is_connected():
                self.conexion.close()
                print('Conexión cerrada ' +
                      time.strftime("%x") + '  ' + time.strftime("%X"))
        except mysql.connector.Error as err:
            print('Error al conectar a la Base de Datos')
            print(err)

    def conectado(self): # Metodo para verificar si la conexion esta activa
        return self.conexion.is_connected()


if __name__ == '__main__':
    print('Soy la clase de conexión a la Base de Datos')
