from os import system
import sys
sys.path.append(r"..\\Inmobiliaria")
from Clases.clasepropiedad import propiedad  # importar la clase propiedad
from Conexion.conexionbd import conexion  # importar la clase conexion
import time
conex = conexion()  # Crear un objeto de la clase conexion
prop = propiedad()  # Crear un objeto de la clase propiedad
salir = False # Variable para salir del programa
Encabezado = "Fecha  " + \
    time.strftime(
        "%x") + "                                          Hora  " + time.strftime("%X")
menu = ("""\
+=====================================================================+
|         Sistema de Gestión y Administración Inmobiliaria            |
+=====================================================================+
|                                                                     |
|   1. Conectarse a la Base de Datos                                  |
|   2. Ingresar una nueva propiedad                                   |
|   3. Modificar datos de propiedad                                   |
|   4. Eliminar datos de propiedad                                    |
|   5. Listar todas las propiedades                                   |
|   6. Listar propiedades disponibles para la venta                   |
|   7. Listar propiedades disponibles para alquiler                   |
|   8. Listar propiedades vendidas                                    |
|   9. Listar propiedades alquiladas                                  |
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
        system("cls")
        if opcion == 1:
            print('Conectando a la Base de Datos...')
            time.sleep(1)
            print()
            conex.conectar()
        elif not conex.conectado():
            print("Debe conectarse a la Base de Datos en la Opción 1")
        else:
            if opcion == 2:                
                time.sleep(0.5)
                prop.insertarPropiedad()
            elif opcion == 3:                 
                print('Para modificar una propiedad, primero se mostrará una lista de todas')
                print()
                continua = input('    PRESIONE UNA TECLA ')
                prop.modificarPropiedad()                
            elif opcion == 4:                 
                print('Para eliminar una propiedad, primero se mostrará una lista de todas')
                print()
                continua = input('    PRESIONE UNA TECLA ')
                prop.eliminarPropiedad()
            elif opcion == 5:                 
                print('A continuación se listarán todas las propiedades...')
                print()
                continua = input('    PRESIONE UNA TECLA ')
                prop.ListarPropiedades()
            elif opcion == 6:                 
                print('A continuación se listarán todas las propiedades disponibles para la venta')
                continua=input('    PRESIONE UNA TECLA ')
                print()
                prop.ListarPropiedadesDispVenta()
            elif opcion == 7:                 
                print('A continuación se listarán todas las propiedades disponibles para alquiler')
                continua = input('    PRESIONE UNA TECLA ')
                print()
                prop.ListarPropiedadesDispAlquiler()
            elif opcion == 8:                 
                print('A continuación se listarán todas las propiedades vendidas')
                continua = input('    PRESIONE UNA TECLA ')
                print()
                prop.ListarPropiedadesVendidas()
            elif opcion == 9:                 
                print('A continuación se listarán todas las propiedades alquiladas')
                continua = input('    PRESIONE UNA TECLA ')
                print()
                prop.ListarPropiedadesAlquiladas()
            elif opcion == 0:
                print('Saliendo del sistema...')
                time.sleep(1)
                conex.desconectar()
                salir = True
                time.sleep(2)
            else:
                print('Numero de opción incorrecto')
        print()
        continua = input('    Presione una tecla para continuar...')
        system("cls")
    except Exception as e:
        print()
        print("    ¡¡ Opción no valida !! ", e)
        continua = input(' Presione una tecla para continuar...')
        time.sleep(1)
        system("cls")
