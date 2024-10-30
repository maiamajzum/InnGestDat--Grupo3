import mysql.connector
from mysql.connector import Error
from datetime import datetime
from colores import *
#-------------------------------------------------------------------------------------------

"""
    Datos necesarios para la conexión DB:

        host="localhost",   
        user="root",        
        password="1sami2astorga", 
        database="Turnero"

"""

userName = None
userPassword = None
conexion = None

def solicitar_datos_conexion():
    global userName, userPassword, conexion
    print(f"{YELLOW}-- Ingrese los accesos para la Base de Datos --{RESET}")

    userName = input(f"{YELLOW}USER: {RESET}")
    userPassword = input(f"{YELLOW}PASSWORD: {RESET}")

    try:
        # Intentar conectarse a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user=userName,
            password=userPassword,
            database="Turnero"
        )
        if conexion.is_connected():
            print(f"{GREEN}Conexión exitosa a la base de datos.{RESET}")
            menu_principalDB()
    except Error as e:
        print(f"{RED}Error al conectar a la base de datos: {e}{RESET}")
        print(f"{YELLOW}Datos de conexión incorrectos. Regresando al menú anterior...{RESET}")
        return  # Regresa al menú anterior

def conectar():
    if conexion is not None and conexion.is_connected():
        return conexion
    else:
        raise Exception(f"{RED}No hay conexión a la base de datos.{RESET}")

def menu_principalDB():
    while True:
        print(f"{YELLOW}\n--- Menú Principal ---{RESET}")
        print("1 -> Pacientes")
        print("2 -> Doctores")
        print("3 -> Turnos Médicos")
        print(f"{RED}\n0 -> Salir{RESET}")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_doctores()
        elif opcion == "3":
            menu_turnos()
        elif opcion == "0":
            print(f"{RED}Saliendo del sistema...{RESET}")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def menu_pacientes():
    while True:
        print("\n--- Menú Pacientes ---")
        print("1 -> Buscar 1 Paciente")
        print("2 -> Mostrar todos los Pacientes")
        print("3 -> Crear un Paciente")
        print("4 -> Actualizar un Paciente")
        print("5 -> Eliminar un Paciente")
        print(f"{RED}\n0 -> Volver al Menú Principal{RESET}")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar_paciente()
        elif opcion == "2":
            mostrar_todos_pacientes()
        elif opcion == "3":
            crear_paciente()
        elif opcion == "4":
            actualizar_paciente()
        elif opcion == "5":
            eliminar_paciente()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def menu_doctores():
    while True:
        print("\n--- Menú Doctores ---")
        print("1 -> Buscar 1 Doctor")
        print("2 -> Mostrar todos los Doctores")
        print("3 -> Buscar Doctor por Especialidad (JOIN)")
        print("4 -> Crear un Doctor")
        print("5 -> Actualizar un Doctor")
        print("6 -> Eliminar un Doctor")
        print(f"{RED}\n0 -> Volver al Menú Principal{RESET}")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar_doctor()
        elif opcion == "2":
            mostrar_todos_doctores()
        elif opcion == "3":
            buscar_doctor_por_especialidad()
        elif opcion == "4":
            crear_doctor()
        elif opcion == "5":
            actualizar_doctor()
        elif opcion == "6":
            eliminar_doctor()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def menu_turnos():
    while True:
        print("\n--- Menú Turnos Médicos ---")
        print("1 -> Buscar Turno por Paciente")
        print("2 -> Mostrar todos los Turnos")
        print("3 -> Crear un Turno")
        print("4 -> Actualizar un Turno")
        print("5 -> Eliminar un Turno")
        print(f"{RED}\n0 -> Volver al Menú Principal{RESET}")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            buscar_turno_por_paciente()
        elif opcion == "2":
            mostrar_todos_turnos()
        elif opcion == "3":
            crear_turno()
        elif opcion == "4":
            actualizar_turno()
        elif opcion == "5":
            eliminar_turno()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# Funciones CRUD para Pacientes

def buscar_paciente():
    dni = input("Ingrese el DNI del paciente: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Paciente WHERE DNI = %s", (dni,))
            paciente = cursor.fetchone()
            if paciente:
                print(f"{GREEN}\nPaciente encontrado: {paciente}{RESET}")
            else:
                print(f"{RED}\nPaciente no encontrado.{RESET}")

def mostrar_todos_pacientes():
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Paciente")
            pacientes = cursor.fetchall()
            if pacientes:
                print(f"{YELLOW}\n--- Lista de Pacientes ---{RESET}")
                for paciente in pacientes:
                    print(f"{GREEN}ID:{RESET} {paciente['id_paciente']}, {GREEN}Nombre:{RESET} {paciente['Nombre']}, {GREEN}Apellido:{RESET} {paciente['Apellido']}, {GREEN}DNI:{RESET} {paciente['DNI']}")
            else:
                print(f"{RED}\nNo se encontraron pacientes.{RESET}")

def crear_paciente():
    dni = input("Ingrese el DNI del paciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("INSERT INTO Paciente (Nombre, Apellido, DNI) VALUES (%s, %s, %s)", (nombre, apellido, dni))
            conexion.commit()
            print(f"{GREEN}\nPaciente creado exitosamente.{RESET}")

def actualizar_paciente():
    dni = input("Ingrese el DNI del paciente a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("UPDATE Paciente SET Nombre = %s WHERE DNI = %s", (nuevo_nombre, dni))
            conexion.commit()
            print(f"{GREEN}\nPaciente actualizado.{RESET}")

def eliminar_paciente():
    dni = input("Ingrese el DNI del paciente a eliminar: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("DELETE FROM Paciente WHERE DNI = %s", (dni,))
            conexion.commit()
            print(f"{GREEN}\nPaciente eliminado.{RESET}")

# Funciones CRUD para Doctores

def buscar_doctor():
    apellido = input("Ingrese el APELLIDO del doctor: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Medico WHERE Apellido = %s", (apellido,))
            doctor = cursor.fetchone()
            if doctor:
                print(f"{YELLOW}\n--- Doctor Encontrado ---{RESET}")
                print(f"{GREEN}ID:{RESET} {doctor['id_medico']}, {GREEN}Nombre:{RESET} {doctor['Nombre']}, {GREEN}Apellido:{RESET} {doctor['Apellido']}")
            else:
                print(f"{RED}\nDoctor no encontrado.{RESET}")

def mostrar_todos_doctores():
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Medico")
            doctores = cursor.fetchall()
            for doctor in doctores:
                print(doctor)

def buscar_doctor_por_especialidad():
    especialidad = input(f"{YELLOW}Ingrese la especialidad: {RESET}")
    print("\n")
    query = """
    SELECT m.Nombre, e.nombre_especialidad
    FROM Medico m
    JOIN Medico_has_Especialidad me ON m.id_medico = me.Medico_id_medico
    JOIN Especialidad e ON me.Especialidad_id_especialidad = e.id_especialidad
    WHERE e.nombre_especialidad = %s
    """
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute(query, (especialidad,))
            doctores = cursor.fetchall()
            for doctor in doctores:
                print(f"Doctor: {doctor['Nombre']}, Especialidad: {doctor['nombre_especialidad']}")

def crear_doctor():
    dni = input("Ingrese el DNI del doctor: ")
    nombre = input("Ingrese el nombre del doctor: ")
    apellido = input("Ingrese el apellido del doctor: ")
    id_especialidad = input("Ingrese el ID de la especialidad: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("INSERT INTO Medico (DNI, Nombre, Apellido, id_especialidad) VALUES (%s, %s, %s, %s)", 
                           (dni, nombre, apellido, id_especialidad))
            conexion.commit()
            print(f"{GREEN}\nDoctor creado exitosamente.{RESET}")

def actualizar_doctor():
    dni = input("Ingrese el DNI del doctor a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("UPDATE Medico SET Nombre = %s WHERE DNI = %s", (nuevo_nombre, dni))
            conexion.commit()
            print(f"{GREEN}\nDoctor actualizado.{RESET}")

def eliminar_doctor():
    dni = input("Ingrese el DNI del doctor a eliminar: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("DELETE FROM Medico WHERE DNI = %s", (dni,))
            conexion.commit()
            print(f"{GREEN}\nDoctor eliminado.{RESET}")

# Funciones CRUD para Turnos Médicos

def buscar_turno_por_paciente():
    dni = input("Ingrese el DNI del paciente: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("""
                SELECT T.id_turno, T.fecha_turno, T.hora_turno, T.Paciente_DNI, E.nombre_especialidad 
                FROM Turno T
                JOIN Especialidad E ON T.Especialidad_id_especialidad = E.id_especialidad
                WHERE T.Paciente_DNI = %s
            """, (dni,))
            turnos = cursor.fetchall()
            
            if turnos:
                print(f"{YELLOW}\n--- Turnos para Paciente DNI {dni} ---{RESET}")
                print(f"{'ID Turno':<10} {'Fecha':<12} {'Hora':<10} {'DNI Paciente':<15} {'Especialidad':<20}")
                print("-" * 70)
                
                for turno in turnos:
                    hora_formateada = turno['hora_turno'].strftime("%H:%M:%S") if isinstance(turno['hora_turno'], datetime) else str(turno['hora_turno'])
                    print(f"{turno['id_turno']:<10} {turno['fecha_turno']:} {hora_formateada:<10} {turno['Paciente_DNI']:<15} {turno['nombre_especialidad']:<20}")
            else:
                print(f"{RED}\nNo se encontraron turnos para este paciente.{RESET}")



def mostrar_todos_turnos():
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            # Consulta con JOIN para obtener el nombre de la especialidad
            cursor.execute("""
                SELECT Turno.id_turno, Turno.fecha_turno, Turno.hora_turno, 
                       Turno.Paciente_DNI, Especialidad.Nombre_Especialidad AS especialidad
                FROM Turno
                JOIN Especialidad ON Turno.Especialidad_id_especialidad = Especialidad.id_especialidad
            """)
            turnos = cursor.fetchall()
            
            # Imprimir encabezado
            print(f"{'ID':<5} {'Fecha':<12} {'Hora':<10} {'DNI Paciente':<15} {'Especialidad'}")
            print("-" * 55)
            
            # Imprimir cada turno con formato
            for turno in turnos:
                fecha_formateada = turno['fecha_turno'].strftime("%Y-%m-%d") if turno['fecha_turno'] else "N/A"
                
                # Formateo de hora
                hora = turno['hora_turno']
                hora_formateada = f"{hora.seconds // 3600:02}:{(hora.seconds // 60) % 60:02}:{hora.seconds % 60:02}" if hora else "N/A"
                
                print(f"{turno['id_turno']:<5} {fecha_formateada:<12} {hora_formateada:<10} "
                      f"{turno['Paciente_DNI']:<15} {turno['especialidad']}")


def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M:%S")
        return True
    except ValueError:
        return False

def crear_turno():
    dni_paciente = input("Ingrese el DNI del paciente: ")
    especialidad = input("Ingrese el ID de la especialidad: ")
    
    # Validación de la fecha
    fecha = input("Ingrese la fecha del turno (YYYY-MM-DD): ")
    if not validar_fecha(fecha):
        print(f"{RED}Formato de fecha incorrecto. Regresando al menú anterior...{RESET}")
        return  # Regresa al menú anterior si el formato es incorrecto

    # Validación de la hora
    hora = input("Ingrese la hora del turno (HH:MM:SS): ")
    if not validar_hora(hora):
        print(f"{RED}Formato de hora incorrecto. Regresando al menú anterior...{RESET}")
        return  # Regresa al menú anterior si el formato es incorrecto
    
    try:
        with conectar() as conexion:
            with conexion.cursor(dictionary=True) as cursor:
                # Verifica si el paciente existe
                cursor.execute("SELECT DNI FROM Paciente WHERE DNI = %s", (dni_paciente,))
                if cursor.fetchone() is None:
                    print(f"{RED}Error: El paciente con DNI {dni_paciente} no existe. Regresando al menú anterior...{RESET}")
                    return
                
                # Inserta el turno en la tabla
                cursor.execute(
                    "INSERT INTO Turno (Paciente_DNI, Especialidad_id_especialidad, fecha_turno, hora_turno) VALUES (%s, %s, %s, %s)", 
                    (dni_paciente, especialidad, fecha, hora)
                )
                conexion.commit()
                
                # Mensaje de confirmación
                print(f"{GREEN}\nTurno creado exitosamente.\nDetalles del turno:")
                print(f"DNI del paciente: {dni_paciente}")
                print(f"ID de especialidad: {especialidad}")
                print(f"Fecha del turno: {fecha}")
                print(f"Hora del turno: {hora}{RESET}")
                
    except Error as e:
        print(f"{RED}Error al crear el turno: {e}{RESET}")

def actualizar_turno():
    id_turno = input("Ingrese el ID del turno a actualizar: ")
    
        # Validación de la fecha
    fecha = input("Ingrese la fecha del turno (YYYY-MM-DD): ")
    if not validar_fecha(fecha):
        print(f"{RED}Formato de fecha incorrecto. Regresando al menú anterior...{RESET}")
        return

    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("UPDATE Turno SET fecha_turno = %s WHERE id_turno = %s", (fecha, id_turno))
            conexion.commit()
            print(f"{GREEN}\nTurno actualizado.{RESET}")


def eliminar_turno():
    id_turno = input("Ingrese el ID del turno a eliminar: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("DELETE FROM Turno WHERE id_turno = %s", (id_turno,))
            conexion.commit()
            print(f"{GREEN}\nTurno eliminado.{RESET}")


