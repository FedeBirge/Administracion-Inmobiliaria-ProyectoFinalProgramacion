import ClaseProp.clasepropiedad as prop  # importamos la clase Propiedad
import time
# importamos la variable conexion del modulo conexionbd
from Conexión.conexionbd import conexion
from os import system


def conectar():
    conexion.connect()
    if conexion.is_connected():
        print('Conexión exitosa ' +
              time.strftime("%x") + '  ' + time.strftime("%X"))


def desconectar():
    if conexion.is_connected():
        conexion.close()
        print('Conexión cerrada ' +
              time.strftime("%x") + '  ' + time.strftime("%X"))


salir = False
Encabezado = "Fecha  " + \
    time.strftime(
        "%x") + "                                          Hora  " + time.strftime("%X")

menu = ("""\
+=====================================================================+
|         Sistema de Gestión y Administración Inmobiliaria            |
+=====================================================================+
|                                                                     |
| 1. Conectarse a la Base de Datos                                    |
| 2. Ingresar una nueva propiedad                                     |
| 3. Modificar datos de prpopiedad                                    |
| 4. Eliminar datos de  propiedad                                     |
| 5. Listar todas las propiedades                                     |
| 6. Listar propiedades disponibles para la venta                     |
| 7. Listar propiedades disponibles para alquiler                     |
| 8. Listar propiedades vendidas                                      |
| 9. Listar propiedades alquiladas                                    |
|                                                                     |
| 0. Salir                                                            |
|                                                                     |
+=====================================================================+\
 """)

while not salir:
    print(Encabezado)
    print(menu)
    try:
        opcion = int(input("Ingrese una opción numérica para operar: "))
        print()
        if opcion == 1:
            print('Conectando a la Base de Datos...')
            conectar()
        elif not conexion.is_connected():
            print("Debe conectarse a la Base de Datos en la Opción 1")
        else:
            if opcion == 2:
                print('Ingresando una nueva propiedad')
            elif opcion == 3:
                print('Modificando datos de propiedad')
            elif opcion == 4:
                print('Eliminando datos de propiedad')
            elif opcion == 5:
                print('Listando todas las propiedades')
            elif opcion == 6:
                print('Listando propiedades disponibles para la venta')
            elif opcion == 7:
                print('Listando propiedades disponibles para alquiler')
            elif opcion == 8:
                print('Listando propiedades vendidas')
            elif opcion == 9:
                print('Listando propiedades alquiladas')
            elif opcion == 0:
                print('Saliendo del sistema')
                desconectar()
                salir = True
                time.sleep(2)
            else:
                print('Numero de opción incorrecto')
        print()
        continua = input('    Presione una tecla para continuar...')
        system("cls")

    except:
        print()
        print("    ¡¡ Opción no valida !! ")
        print()
        continua = input(' Presione una tecla para continuar...')
        time.sleep(1)
        system("cls")
