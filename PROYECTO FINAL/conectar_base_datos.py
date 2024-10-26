from mysql import connector
from mysql.connector import Error

def conectar_base_datos(user, password):
    try:
        conexion = connector.connect(
            host="localhost",
            user=user,
            password=password,
            database="Turnero"
        )
        print("Conexión exitosa a la base de datos.")
        return conexion
    except Error as e:
        print("Error al conectar con la base de datos:", e)
        return None