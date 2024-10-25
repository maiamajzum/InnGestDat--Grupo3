from mysql import connector
from mysql.connector import Error

# modificar los datos entre comillas por los correspondientes con sus credenciales de acceso configuradas en la instalación de MySQL
def conectar_base_datos():
    try:
        conexion = connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="Turnero"
        )
        print("Conexión exitosa a la base de datos.")
        return conexion
    except Error as e:
        print("Error al conectar con la base de datos:", e)
        print("Por favor, configure los datos de conexión y pruebe nuevamente o vuelva al menú principal.")
        return None