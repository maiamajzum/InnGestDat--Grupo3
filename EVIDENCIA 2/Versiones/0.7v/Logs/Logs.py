import sys
import os
import pickle

def errorLog(usuario, clave):
    # Importar timeNow aquí para evitar la importación circular
    from Login import timeNow
    hora_actual = timeNow()

    with open('logs.txt', 'a') as file:
        file.write(f"Acceso Fallido -> Usuario: {usuario} // Password: {clave} // Hora: {hora_actual}\n")

def accesLog(usuario, clave):
    from Login import timeNow
    hora_actual = [timeNow()]
    
        
    with open('accesos.ispc', 'ab') as file:  # 'ab' para agregar datos en modo binario
        pickle.dump(hora_actual[-1], file) 
    
    return hora_actual


def readLog():
    horas = []  # Inicializa la lista para almacenar las horas
    # Intentar leer las horas anteriores desde el archivo
    try:
        with open('accesos.ispc', 'rb') as file:  # 'rb' para leer en modo binario
            while True:
                try:
                    horas.append(pickle.load(file))
                except EOFError:
                    break  # Termina la lectura al alcanzar el final del archivo
    except FileNotFoundError:
        print("El archivo no existe. Se creará uno nuevo.")
        return []  # Retorna una lista vacía si no se encuentra el archivo

    return horas  # Retorna la lista de horas leídas
