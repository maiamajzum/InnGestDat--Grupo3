# cRud -> Read (Buscar, para los compas)
import sys
import os
from tabulate import tabulate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Conexion")))
from Conexion import conectar_DB


def read():
    con = conectar_DB()
    cursor = con.cursor()

    #status = 0 # Una mausque herramienta misteriosa, que nos ayudará mas tarde

    print("Para continuar, INGRESE un EMAIL o USERNAME: ")    
    uSelection = input()

    cursor.execute("SELECT * FROM Evidencia2.usuario WHERE email = %s OR username = %s;", (uSelection, uSelection))
    user = cursor.fetchone()


    if user:
        # Convertir la tupla en una lista para que printTable funcione
        printTable([user])  # Pasamos una lista que contiene la tupla
        return user
        
    else: 
        print("No se encontró ese EMAIL o USERNAME")
    
    #return status
    con.close()


def readAll():
    con = conectar_DB()
    cursor = con.cursor()

    cursor.execute("SELECT * FROM Evidencia2.usuario;")
    users = cursor.fetchall()

    if users:
        tabla_user = [[user[0], user[1], user[2], user[3]] for user in users]
        
        
        printTable(tabla_user)
        #headers = ["ID", "Username", "Password", "Email"]
        #print(tabulate(tabla_user, headers=headers, tablefmt="grid"))


    con.close()


def printTable(tabla_user):
    
        # Tabla formateada
    headers = ["ID", "Username", "Password", "Email"]
    print(tabulate(tabla_user, headers=headers, tablefmt="grid"))