import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Crud")))

from Read import readAll
from Read import read
from Delete import delete
from Modify import modify
from Registro import registrarUsuario
from Login import userOut
from Logs import readLog

def menu(acceso_id):
    while True:
        print("\n- MENÚ -\n")
        print("1 -> Crear Usuario.")
        print("2 -> Buscar Usuario.")
        print("3 -> Buscar TODOS los Usuarios.")
        print("4 -> Modificar Usuario.")
        print("5 -> Eliminar Usuario.")
        #print("6 ->  Leer Archivo Binario.")
        print("0 -> Salir.")

        uSelection = input("Seleccione una opción: ")

        match uSelection:
            case "1":
                registrarUsuario()
            case "2":
                read()
            case "3":
                readAll()
            case "4":
                modify()
            case "5":
                delete()
            #case "6":
            #   readLog()
            case "0":
                userOut(acceso_id)  # Salida del usuario
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Inténtelo nuevamente.")
