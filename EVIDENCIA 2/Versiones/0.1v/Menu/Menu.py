import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Crud")))
from Read import readAll
from Read import read

def menu():
    
    print("- MENÚ -\n")
    print("1 -> Crear Usuario.")
    print("2 -> Buscar Usuario.")
    print("3 -> Buscar TODOS los Usuarios.")
    print("4 -> Modificar Usuario.")
    print("5 -> Eliminar Usuario.")

    uSelection = input()

    match uSelection:
        case "1":
            print("1")
        case "2":
            read()
        case "3":
            readAll()
        case "4":
            print("4")
        case "5":
            print("5")

