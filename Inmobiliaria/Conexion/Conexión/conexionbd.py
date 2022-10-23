import mysql.connector
try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Feddu#1985',
        db='Inmobiliaria'
    )
   
except:
    print('Error al conectar a la Base de Datos')

if __name__ == '__main__':
    print('Soy el modulo de conexión a la Base de Datos')
    
        