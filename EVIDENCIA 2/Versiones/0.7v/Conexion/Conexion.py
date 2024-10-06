import mysql.connector

# modificar los datos entre comillas por los correspondientes a su usuario de MYSQL
def conectar_DB():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123", #CAMBIEN LA CONTRASEÑA A LAS DE USTEDES!
        database="Evidencia2"
    )
