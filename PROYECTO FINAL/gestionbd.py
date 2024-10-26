import mysql.connector
from conectar_base_datos import conectar_base_datos
from datetime import datetime  

def gestionbd(cursor, conn):
    # Código para gestionar la base de datos
    pass

def verificar_y_saludar_paciente(cursor, dni):
    cursor.execute("SELECT Nombre, Apellido FROM Paciente WHERE DNI = %s", (dni,))
    paciente = cursor.fetchone()
    
    if paciente:
        print(f"Hola {paciente[0]} {paciente[1]}, ¡bienvenido/a!")
        return True
    else:
        print("El DNI ingresado no existe. Por favor, ingresa un DNI válido.")
        return False

def listar_especialidades(cursor):
    cursor.execute("SELECT id_especialidad, Nombre_Especialidad FROM Especialidad")
    especialidades = cursor.fetchall()

    if especialidades:
        print("Especialidades disponibles:")
        for especialidad in especialidades:
            print(f"ID: {especialidad[0]}, Nombre: {especialidad[1]}")
    else:
        print("No hay especialidades disponibles.")
    
    return especialidades

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False
    
def mostrar_turnos_disponibles(cursor, dni):
    cursor.execute("SELECT id_paciente FROM Paciente WHERE DNI = %s", (dni,))
    paciente = cursor.fetchone()
    
    if paciente is None:
        print("No se encontró un paciente con el DNI ingresado.")
        return

    id_paciente = paciente[0]

    cursor.execute("""SELECT t.id_turno, t.fecha_turno, t.hora_turno, e.Nombre_Especialidad 
                      FROM Turno t 
                      JOIN Especialidad e ON t.Especialidad_id_especialidad = e.id_especialidad
                      WHERE t.Paciente_DNI = %s""", (dni,))
    
    turnos = cursor.fetchall()
    
    if not turnos:
        print("No hay turnos disponibles para el paciente.")
        return
    
    print("Turnos disponibles:")
    for turno in turnos:
        print(f"ID: {turno[0]}, Fecha: {turno[1]}, Hora: {turno[2]}, Especialidad: {turno[3]}")

def crear_turno(conn):
    cursor = conn.cursor()
    while True:
        dni = input("Ingresa el DNI del paciente: ")
        if verificar_y_saludar_paciente(cursor, dni):
            break
    
    listar_especialidades(cursor)
    
    especialidad_id = int(input("Ingresa el ID de la especialidad: "))
    cursor.execute("SELECT * FROM Especialidad WHERE id_especialidad = %s", (especialidad_id,))
    if not cursor.fetchone():
        print("La especialidad ingresada no existe. Por favor, intenta de nuevo.")
        cursor.close()
        return
    
    cursor.close()

    while True:
        fecha_turno = input("Ingresa la fecha del turno (YYYY-MM-DD): ")
        if validar_fecha(fecha_turno):
            break
        else:
            print("La fecha ingresada no es válida. Por favor, ingresa una fecha en el formato correcto.")
    
    while True:
        hora_turno = input("Ingresa la hora del turno (HH:MM): ")
        if validar_hora(hora_turno):
            break
        else:
            print("La hora ingresada no es válida. Por favor, ingresa una hora en el formato correcto.")
    
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Turno (Paciente_DNI, fecha_turno, hora_turno, Especialidad_id_especialidad) VALUES (%s, %s, %s, %s)", 
                       (dni, fecha_turno, hora_turno, especialidad_id))
        conn.commit()
        print("Turno creado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al crear el turno: {err}")
        conn.rollback()
    finally:
        cursor.close()

def leer_turnos(conn):
    cursor = conn.cursor()
    while True:
        dni = input("Ingresa tu DNI para consultar los turnos: ")
        if verificar_y_saludar_paciente(cursor, dni):
            mostrar_turnos_disponibles(cursor, dni)
            break

def modificar_turno(conn):
    cursor = conn.cursor()
    while True:
        dni = input("Ingresa tu DNI para modificar un turno: ")
        if verificar_y_saludar_paciente(cursor, dni):
            mostrar_turnos_disponibles(cursor, dni)
            break

    while True:
        id_turno = int(input("Ingresa el ID del turno a modificar: "))
        
        cursor.execute("SELECT * FROM Turno WHERE id_turno = %s AND Paciente_DNI = %s", (id_turno, dni))
        if not cursor.fetchone():
            print("El turno ingresado no existe para el paciente. Intenta nuevamente.")
            continue
        else:
            break

    while True:
        fecha_turno = input("Ingresa la nueva fecha del turno (YYYY-MM-DD): ")
        if validar_fecha(fecha_turno):
            break
        else:
            print("La fecha ingresada no es válida. Asegúrate de seguir el formato YYYY-MM-DD.")

    while True:
        hora_turno = input("Ingresa la nueva hora del turno (HH:MM): ")
        if validar_hora(hora_turno):
            break
        else:
            print("La hora ingresada no es válida. Asegúrate de seguir el formato HH:MM.")

    while True:
        especialidad_id = int(input("Ingresa el ID de la nueva especialidad: "))
        cursor.execute("SELECT * FROM Especialidad WHERE id_especialidad = %s", (especialidad_id,))
        if cursor.fetchone():
            break

    try:
        cursor.execute("UPDATE Turno SET fecha_turno = %s, hora_turno = %s, Especialidad_id_especialidad = %s WHERE id_turno = %s", 
                       (fecha_turno, hora_turno, especialidad_id, id_turno))
        conn.commit()
        print("Turno modificado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al modificar el turno: {err}")
        conn.rollback()
    finally:
        cursor.close()

def eliminar_turno(conn):
    cursor = conn.cursor()
    while True:
        dni = input("Ingresa tu DNI para eliminar un turno: ")
        if verificar_y_saludar_paciente(cursor, dni):
            mostrar_turnos_disponibles(cursor, dni)
            break
        
    id_turno = int(input("Ingresa el ID del turno que deseas eliminar: "))
    try:
        cursor.execute("DELETE FROM Turno WHERE id_turno = %s AND Paciente_DNI = %s", (id_turno, dni))
        conn.commit()
        print("Turno eliminado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar el turno: {err}")
        conn.rollback()
    finally:
        cursor.close()

def mainbd():
    user = input("Ingrese el nombre de usuario configurado en la instalación de MySQL: ")
    password = input("Ingrese la clave de MySQL: ")
    conn = conectar_base_datos(user, password)

    if conn is None:
        print("No se pudo conectar a la base de datos. Revisa tus credenciales.")
        return None, None  # Devolver None si no se pudo conectar

    cursor = conn.cursor()  # Crear cursor aquí

    while True:
        print("\n1. Crear Turno")
        print("2. Leer Turnos")
        print("3. Modificar Turno")
        print("4. Eliminar Turno")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        match opcion:
            case '1':
                crear_turno(conn)
            case '2':
                leer_turnos(conn)
            case '3':
                modificar_turno(conn)
            case '4':
                eliminar_turno(conn)
            case '5':
                print("Hasta luego!")
                cursor.close()  # Cerrar el cursor antes de salir
                return cursor, conn  # Retornar el cursor y la conexión antes de salir
            case _:
                print("Opción no válida. Por favor, intenta de nuevo.")

        while True:
            otra_accion = input("¿Deseas realizar otra acción? Ingresa 's' para Sí o 'n' para No: ").strip().lower()
            if otra_accion == 's':
                break
            elif otra_accion == 'n':
                print("Hasta luego!")
                cursor.close()  # Cerrar el cursor aquí también
                return cursor, conn  # Retornar el cursor y la conexión
            else:
                print("Entrada no válida. Por favor, ingresa 's' para Sí o 'n' para No.")

    cursor.close()  # Cerrar el cursor
    return cursor, conn  # Retornar el cursor y la conexión al final


      

if __name__ == "__main__":
    mainbd()
