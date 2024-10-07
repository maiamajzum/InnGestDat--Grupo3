import mysql.connector

# modificar los datos entre comillas por los correspondientes a su usuario de MYSQL
def conectar_DB():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234", #COLOCAR CLAVE DE USUARIO
        database="Evidencia2"
    )
