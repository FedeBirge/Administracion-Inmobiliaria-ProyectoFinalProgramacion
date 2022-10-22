import ClaseProp.clasepropiedad as prop  # importamos la clase Propiedad
import time
from os import system

salir = False
Encabezado = "Fecha  " + \
    time.strftime(
        "%x") + "                                          Hora  " + time.strftime("%X")

menu = ("""\
+=====================================================================+
|         Sistema de Gestión y Administración Inmobiliaria            |
+=====================================================================+
|                                                                     |
| 1. Conectarse al Base de Datos                                      |
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
        opcion = int(input("Ingrese una opcion: "))
        print()
        if opcion == 1:
            print('Conectando a la Base de Datos...')
        elif opcion == 2:
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
            salir = True
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
        system("cls")
