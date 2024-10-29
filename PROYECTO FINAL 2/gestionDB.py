import mysql.connector
from colores import *
#-------------------------------------------------------------------------------------------

def conectar():
        return mysql.connector.connect(
        host="localhost",   
        user="root",        
        password="1sami2astorga", 
        database="Turnero"
    )

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
            cursor.execute("SELECT * FROM Turno WHERE PACIENTE_DNI = %s", (dni,))
            turnos = cursor.fetchall()
            if turnos:
                print(f"{YELLOW}\n--- Turnos para Paciente DNI {dni} ---{RESET}")
                for turno in turnos:
                    print(f"{GREEN}ID Turno:{RESET} {turno['id_turno']}, {GREEN}Fecha:{RESET} {turno['fecha_turno']},{GREEN}Hora: {RESET}{turno['hora_turno'],} {GREEN}DNI Paciente:{RESET} {turno['Paciente_DNI']}, {GREEN}Especialidad: {RESET} {turno['Especialidad_id_especialidad']} ")
            else:
                print(f"{RED}\nNo se encontraron turnos para este paciente.{RESET}")

def mostrar_todos_turnos():
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Turno")
            turnos = cursor.fetchall()
            for turno in turnos:
                print(turno)

def crear_turno():
    dni_paciente = input("Ingrese el DNI del paciente: ")
    dni_doctor = input("Ingrese el DNI del doctor: ")
    fecha = input("Ingrese la fecha del turno (YYYY-MM-DD): ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("INSERT INTO Turno (dni_paciente, dni_doctor, fecha) VALUES (%s, %s, %s)", 
                           (dni_paciente, dni_doctor, fecha))
            conexion.commit()
            print(f"{GREEN}\nTurno creado exitosamente.{RESET}")

def actualizar_turno():
    id_turno = input("Ingrese el ID del turno a actualizar: ")
    nueva_fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("UPDATE Turno SET fecha = %s WHERE id = %s", (nueva_fecha, id_turno))
            conexion.commit()
            print(f"{GREEN}\nTurno actualizado.{RESET}")

def eliminar_turno():
    id_turno = input("Ingrese el ID del turno a eliminar: ")
    with conectar() as conexion:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("DELETE FROM Turno WHERE id = %s", (id_turno,))
            conexion.commit()
            print(f"{GREEN}\nTurno eliminado.{RESET}")


