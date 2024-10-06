import sys
import os
from Read import read

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Conexion")))
from Conexion import conectar_DB


def delete():
    con = conectar_DB()
    cursor = con.cursor()
    print("Para ELIMINAR un USUARIO, ingrese EMAIL o USERNAME")

    uSelection = input()

    # En una futura versión, deberíamos utilizar directamente el método READ() para ahorrar código
    cursor.execute("SELECT * FROM Evidencia2.usuario WHERE email = %s OR username = %s;", (uSelection, uSelection))
    user = cursor.fetchone()

    if user:
        print("Está por ELIMINAR al USUARIO del sistema.")
        confirmation = input("Desea continuar? Y/N: ")

        if confirmation.lower() == "y": #Saneamos las minusculas
            cursor.execute("DELETE FROM Evidencia2.usuario WHERE email = %s OR username = %s;", (uSelection, uSelection))
            con.commit()  # No nos olvidemos del .commit()
            print("Usuario eliminado exitosamente.")
        else:
            print("Operación de eliminación cancelada.")
    else:
        print("No se encontró el usuario con ese EMAIL o USERNAME.")

    con.close()
