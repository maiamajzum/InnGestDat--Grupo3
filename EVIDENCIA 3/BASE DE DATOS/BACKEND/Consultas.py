import mysql.connector
import pandas as pd
# Conectar a la base de datos MySQL
from conectar_base_datos import conectar_base_datos

# Crear la conexión a la base de datos
conn = conectar_base_datos()
cursor = conn.cursor()

# Función para ejecutar la consulta y mostrar los resultados en formato tabla
def ejecutar_consulta(consulta):
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    columnas = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
    tabla = pd.DataFrame(resultado, columns=columnas)  # Convertir a formato tabla con pandas
    print("\nResultados:\n")
    print(tabla)

# Menú de consultas
def mostrar_menu():
    print("\nSeleccione una consulta para visualizar:")
    print("1. Mostrar todos los datos de la tabla Paciente")
    print("2. Mostrar id_paciente y DNI de la tabla Paciente")
    print("3. Mostrar médicos por horario (Horario_id_Horario = 1)")
    print("4. Mostrar turnos de una especialidad y horario (Especialidad_id_especialidad = 3 y hora_turno entre 10 y 14)")
    print("5. Mostrar los primeros 3 médicos cuyos nombres empiezan con 'A'")
    print("6. Mostrar pacientes que tengan turnos en la especialidad 'Clínica Médica'")
    print("7. Salir")

# Pregunta si desea realizar otra consulta
def preguntar_otro_intento():
    respuesta = input("\n¿Desea realizar otra consulta? (s/n): ").lower()
    return respuesta == 's'

# Función principal del menú
def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("\nIngrese el número de la consulta que desea realizar: ")

        if opcion == "1":
            consulta = "SELECT * FROM paciente;"
            ejecutar_consulta(consulta)

        elif opcion == "2":
            consulta = "SELECT id_paciente, DNI FROM paciente;"
            ejecutar_consulta(consulta)

        elif opcion == "3":
            consulta = "SELECT * FROM medico WHERE Horario_id_Horario = 1;"
            ejecutar_consulta(consulta)

        elif opcion == "4":
            consulta = "SELECT * FROM turno WHERE Especialidad_id_especialidad = 3 AND hora_turno BETWEEN 10 AND 14;"
            ejecutar_consulta(consulta)

        elif opcion == "5":
            consulta = "SELECT * FROM medico WHERE Nombre LIKE 'A%' LIMIT 3;"
            ejecutar_consulta(consulta)

        elif opcion == "6":
            consulta = """
                SELECT paciente.Nombre 
                FROM paciente
                INNER JOIN turno ON paciente.DNI = turno.Paciente_DNI
                INNER JOIN especialidad ON turno.Especialidad_id_especialidad = especialidad.id_especialidad
                WHERE especialidad.Nombre_Especialidad = 'Clínica Médica';
            """
            ejecutar_consulta(consulta)

        elif opcion == "7":
            print("Saliendo del programa.")
            continuar = False

        else:
            print("Opción no válida. Inténtelo de nuevo.")

        # Preguntar si desea continuar solo si no seleccionó salir
        if continuar:
            continuar = preguntar_otro_intento()

# Ejecutar el menú
if __name__ == "__main__":
    main()

# Cerrar la conexión cuando se termine el programa
cursor.close()
conn.close()
