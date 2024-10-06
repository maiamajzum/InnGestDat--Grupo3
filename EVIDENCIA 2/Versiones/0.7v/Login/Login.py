from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Conexion")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Logs")))
from Conexion import conectar_DB
from Logs import errorLog
from Logs import accesLog

def login():

    con = conectar_DB()
    cursor = con.cursor()

    print("¡Bienvenido a INSTATURNO!")

    usuario = input("Ingrese su USERNAME: ")
    clave = input("Ingrese su PASSWORD: ")

    # Consultar en la tabla usuario
    cursor.execute("SELECT ID FROM Evidencia2.usuario WHERE username = %s AND password = %s;", (usuario, clave))
    acces = cursor.fetchone()

    if acces:
        print(f"Acceso concedido, bienvenido {usuario}")
        acceso_id = userIn(acces[0])  # Obtener el acceso_id del usuario logueado
        accesLog(usuario, clave)
        return acceso_id  # Retornar el acceso_id para usarlo luego

    else:
        print("Usuario o clave incorrectos")
        errorLog(usuario, clave)
        return None  # Retornar None si el login falla

def timeNow():
    # Obtener fecha y hora actual
    timenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timenow

def userIn(usuario_id):
    con = conectar_DB()
    cursor = con.cursor()

    fecha_ingreso = timeNow()

    # Insertar fecha de ingreso en la tabla accesos
    query = "INSERT INTO accesos (fechaIngreso, usuarioLogueado) VALUES (%s, %s)"
    cursor.execute(query, (fecha_ingreso, usuario_id))
    con.commit()

    acceso_id = cursor.lastrowid  # Retorna el ID para poder actualizar la salida

    con.close()
    return acceso_id

def userOut(acceso_id):
    con = conectar_DB()
    cursor = con.cursor()

    fecha_salida = timeNow()

    # Actualizar la fecha de salida en la tabla accesos
    query = "UPDATE accesos SET fechaSalida = %s WHERE ID = %s"
    cursor.execute(query, (fecha_salida, acceso_id))
    con.commit()

    con.close()

