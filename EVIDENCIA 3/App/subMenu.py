import mysql.connector
#-------------------------------------------------------------------------------------------

# Mati esta parte no hace falta la podes eliminar solo la cree para testear
conexion = mysql.connector.connect(
    host="localhost",   
    user="root",        
    password="123456789", 
    database="Turnero"    
)
#------------------------------------------------------------------------------------------
cursor = conexion.cursor(dictionary=True)

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Pacientes")
        print("2. Doctores")
        print("3. Turnos Médicos")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_doctores()
        elif opcion == "3":
            menu_turnos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def menu_pacientes():
    while True:
        print("\n--- Menú Pacientes ---")
        print("1. Buscar 1 Paciente")
        print("2. Mostrar todos los Pacientes")
        print("3. Crear un Paciente")
        print("4. Actualizar un Paciente")
        print("5. Eliminar un Paciente")
        print("0. Volver al Menú Principal")
        
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
        print("1. Buscar 1 Doctor")
        print("2. Mostrar todos los Doctores")
        print("3. Buscar Doctor por Especialidad (JOIN)")
        print("4. Crear un Doctor")
        print("5. Actualizar un Doctor")
        print("6. Eliminar un Doctor")
        print("0. Volver al Menú Principal")
        
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
        print("1. Buscar Turno por Paciente")
        print("2. Mostrar todos los Turnos")
        print("3. Crear un Turno")
        print("4. Actualizar un Turno")
        print("5. Eliminar un Turno")
        print("0. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")

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
    cursor.execute("SELECT * FROM pacientes WHERE dni = %s", (dni,))
    paciente = cursor.fetchone()
    if paciente:
        print(f"Paciente encontrado: {paciente}")
    else:
        print("Paciente no encontrado.")

def mostrar_todos_pacientes():
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    for paciente in pacientes:
        print(paciente)

def crear_paciente():
    dni = input("Ingrese el DNI del paciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    cursor.execute("INSERT INTO pacientes (dni, nombre, edad) VALUES (%s, %s, %s)", (dni, nombre, edad))
    conexion.commit()
    print("Paciente creado exitosamente.")

def actualizar_paciente():
    dni = input("Ingrese el DNI del paciente a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    cursor.execute("UPDATE pacientes SET nombre = %s WHERE dni = %s", (nuevo_nombre, dni))
    conexion.commit()
    print("Paciente actualizado.")

def eliminar_paciente():
    dni = input("Ingrese el DNI del paciente a eliminar: ")
    cursor.execute("DELETE FROM pacientes WHERE dni = %s", (dni,))
    conexion.commit()
    print("Paciente eliminado.")

# Funciones CRUD para Doctores

def buscar_doctor():
    dni = input("Ingrese el DNI del doctor: ")
    cursor.execute("SELECT * FROM doctores WHERE dni = %s", (dni,))
    doctor = cursor.fetchone()
    if doctor:
        print(f"Doctor encontrado: {doctor}")
    else:
        print("Doctor no encontrado.")

def mostrar_todos_doctores():
    cursor.execute("SELECT * FROM doctores")
    doctores = cursor.fetchall()
    for doctor in doctores:
        print(doctor)

def buscar_doctor_por_especialidad():
    especialidad = input("Ingrese la especialidad: ")
    query = """
    SELECT d.nombre, e.nombre_especialidad
    FROM doctores d
    JOIN especialidades e ON d.id_especialidad = e.id
    WHERE e.nombre_especialidad = %s
    """
    cursor.execute(query, (especialidad,))
    doctores = cursor.fetchall()
    for doctor in doctores:
        print(f"Doctor: {doctor['nombre']}, Especialidad: {doctor['nombre_especialidad']}")

def crear_doctor():
    dni = input("Ingrese el DNI del doctor: ")
    nombre = input("Ingrese el nombre del doctor: ")
    id_especialidad = input("Ingrese el ID de la especialidad: ")
    cursor.execute("INSERT INTO doctores (dni, nombre, id_especialidad) VALUES (%s, %s, %s)", (dni, nombre, id_especialidad))
    conexion.commit()
    print("Doctor creado exitosamente.")

def actualizar_doctor():
    dni = input("Ingrese el DNI del doctor a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    cursor.execute("UPDATE doctores SET nombre = %s WHERE dni = %s", (nuevo_nombre, dni))
    conexion.commit()
    print("Doctor actualizado.")

def eliminar_doctor():
    dni = input("Ingrese el DNI del doctor a eliminar: ")
    cursor.execute("DELETE FROM doctores WHERE dni = %s", (dni,))
    conexion.commit()
    print("Doctor eliminado.")

# Funciones CRUD para Turnos Médicos

def buscar_turno_por_paciente():
    dni = input("Ingrese el DNI del paciente: ")
    cursor.execute("SELECT * FROM turnos WHERE dni_paciente = %s", (dni,))
    turnos = cursor.fetchall()
    for turno in turnos:
        print(turno)

def mostrar_todos_turnos():
    cursor.execute("SELECT * FROM turnos")
    turnos = cursor.fetchall()
    for turno in turnos:
        print(turno)

def crear_turno():
    dni_paciente = input("Ingrese el DNI del paciente: ")
    dni_doctor = input("Ingrese el DNI del doctor: ")
    fecha = input("Ingrese la fecha del turno: ")
    cursor.execute("INSERT INTO turnos (dni_paciente, dni_doctor, fecha) VALUES (%s, %s, %s)", (dni_paciente, dni_doctor, fecha))
    conexion.commit()
    print("Turno creado exitosamente.")

def actualizar_turno():
    id_turno = input("Ingrese el ID del turno a actualizar: ")
    nueva_fecha = input("Ingrese la nueva fecha: ")
    cursor.execute("UPDATE turnos SET fecha = %s WHERE id = %s", (nueva_fecha, id_turno))
    conexion.commit()
    print("Turno actualizado.")

def eliminar_turno():
    id_turno = input("Ingrese el ID del turno a eliminar: ")
    cursor.execute("DELETE FROM turnos WHERE id = %s", (id_turno,))
    conexion.commit()
    print("Turno eliminado.")

# Iniciar el programa. ver si le cambiamos el nombre ?
menu_principal()


conexion.close()



