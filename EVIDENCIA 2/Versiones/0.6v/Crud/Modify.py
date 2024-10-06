import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Conexion")))
from Conexion import conectar_DB


def modify():
    con = conectar_DB()
    cursor = con.cursor()
    
    print("Para poder MODIFICAR un USUARIO, primero ingrese un EMAIL o NOMBRE")
    uSelection = input()

    cursor.execute("SELECT * FROM Evidencia2.usuario WHERE email = %s OR username = %s;", (uSelection, uSelection))
    user = cursor.fetchone()

    if user:
        print('1 -> Username')
        print('2 -> Password')
        print('3 -> Email\n')

        uS = input('Qué campo desea MODIFICAR: ')

        match uS:
            case "1":
                nuevo_username = input("Ingrese el nuevo Username: ")
                cursor.execute("UPDATE Evidencia2.usuario SET username = %s WHERE email = %s OR username = %s;", (nuevo_username, uSelection, uSelection))
                print("Username modificado exitosamente.")

            case "2":
                nuevo_password = input("Ingrese el nuevo Password: ")
                cursor.execute("UPDATE Evidencia2.usuario SET password = %s WHERE email = %s OR username = %s;", (nuevo_password, uSelection, uSelection))
                print("Password modificado exitosamente.")

            case "3":
                nuevo_email = input("Ingrese el nuevo Email: ")
                cursor.execute("UPDATE Evidencia2.usuario SET email = %s WHERE email = %s OR username = %s;", (nuevo_email, uSelection, uSelection))
                print("Email modificado exitosamente.")

            case _:
                print("Opción no válida.")

        con.commit()
    else:
        print("No se encontró el usuario con ese EMAIL o USERNAME.")

    con.close()