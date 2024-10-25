from clases import *
import os
from datetime import datetime
from gestionUsuario import *
from colores import *


"""
 
▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▖ ▗▄▄▄  ▗▄▖  ▗▄▄▖
▐▛▚▞▜▌▐▌     █ ▐▌ ▐▌▐▌  █▐▌ ▐▌▐▌   
▐▌  ▐▌▐▛▀▀▘  █ ▐▌ ▐▌▐▌  █▐▌ ▐▌ ▝▀▚▖
▐▌  ▐▌▐▙▄▄▖  █ ▝▚▄▞▘▐▙▄▄▀▝▚▄▞▘▗▄▄▞▘

"""



def leerAccesos(archivo="accesos.ispc"):
    try:
        with open(archivo, "rb") as archivo_binario:
            accesos = pickle.load(archivo_binario)
    except (FileNotFoundError, EOFError):
        accesos = []
    return accesos

def crearAcceso(id: int, usuarioLogueado: Usuario, archivo="accesos.ispc") -> None:
    # Crear las fechas de ingreso y salida como ejemplo
    fechaIngreso = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fechaSalida = "N/A"  # Se puede actualizar más tarde

    # Crear un objeto Acceso, asegurando que usuarioLogueado sea de tipo Usuario
    acceso = Acceso(id, fechaIngreso, fechaSalida, usuarioLogueado)

    try:
        accesos_lista = leerAccesos(archivo)  # Leer el archivo, si no existe, retorna lista vacía
        accesos_lista.append(acceso)  # Agregar el nuevo acceso a la lista

        # Guardar los accesos en el archivo binario
        with open(archivo, "wb") as archivo_binario:
            pickle.dump(accesos_lista, archivo_binario)

        #print(f"\nAcceso creado y guardado exitosamente: \n{acceso}")

    except Exception as e:
        print(f"\nError al intentar crear el acceso: {e}")

def ingreso(userName: str, userPassword: str, archivo="usuarios.ispc") -> None:
    # Leer la lista de usuarios
    usuarios_lista = leerUsuario(archivo)

    for usuario in usuarios_lista:
        if usuario.getUsername() == userName and usuario.getPassword() == userPassword:
            print(f"{MAGENTA}\n¡Hola, {userName}! Bienvenido/a.{RESET}")
            print(f"{YELLOW}    ____   ____ ______ _   __ _    __ ______ _   __ ____ ____   ____  ")
            print("   / __ ) /  _// ____// | / /| |  / // ____// | / //  _// __ \ / __ \ ")
            print("  / __  | / / / __/  /  |/ / | | / // __/  /  |/ / / / / / // / / / ")
            print(" / /_/ /_/ / / /___ / /|  /  | |/ // /___ / /|  /_/ / / /_/ // /_/ /  ")
            print("/_____//___//_____//_/ |_/   |___//_____//_/ |_//___//_____/ \____/   ")
            print(f"                                                                     {RESET}")

            # Crear un nuevo acceso con el ID del usuario y el nombre del usuario logueado
            usuarioLogeado = retornarUsuario(userName)

            if usuarioLogeado:
                crearAcceso(usuario.getId(), usuarioLogeado)  # Usamos getUsername() en lugar de userName
            return

    # Mensaje de error si no se encuentra el usuario o la contraseña es incorrecta
    print(f"{RED}\nNombre de usuario o contraseña incorrectos.{RESET}")
    logs(userName, userPassword)  # Asegúrate de que logs registre el nombre que se intentó usar

def retornarUsuario(userName: str, archivo="usuarios.ispc"):
    # Leer la lista de usuarios desde el archivo
    usuarios_lista = leerUsuario(archivo)

    # Buscar al usuario por el nombre de usuario
    for usuario in usuarios_lista:
        if usuario.getUsername() == userName:
            return usuario  # Retornar el objeto Usuario si se encuentra

    # Si no se encuentra, retornar None
    return None


def logs(userName: str, userPassword: str, archivo_log="logs.txt"):
    
    if not os.path.exists(archivo_log):
        with open(archivo_log, 'w') as archivo:
            archivo.write("Registro de ingresos de usuarios\n")
            archivo.write("---------------------------------\n")
    
    fecha_hora_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Guarda -> user y fecha
    with open(archivo_log, 'a') as archivo:
        archivo.write(f"Usuario: {userName} - Password: {userPassword} - Fecha y hora: {fecha_hora_actual}\n")

def mostrarAccesos(archivo='accesos.ispc'):
    # Intentar leer el archivo binario de accesos
    try:
        accesos_lista = leerAccesos(archivo)
        if not accesos_lista:
            print(f"{RED}No se encontraron accesos registrados.{RESET}")
        else:
            for acceso in accesos_lista:
                print(f"{GREEN}{acceso}{RESET}")  # Esto mostrará cada acceso utilizando el método __str__ de la clase Acceso
    except FileNotFoundError:
        print("El archivo de accesos no existe.")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo de accesos: {e}")

def mostrarLogs():
    # Verificar si el archivo logs.txt existe
    if os.path.exists("logs.txt"):
        # Abrir el archivo en modo lectura
        with open("logs.txt", "r") as file:
            logs = file.readlines()  # Leer todas las líneas del archivo
            # Mostrar cada log en consola
            for log in logs:
                print(f"{RED}")
                print(log.strip())  # Imprimir cada línea sin saltos de línea
                print(f"{RESET}")
    else:
        print("No hay logs disponibles.")


""" 
    
        ▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖ ▗▄▄▖
        ▐▛▚▞▜▌▐▌   ▐▛▚▖▐▌▐▌ ▐▌▐▌   
        ▐▌  ▐▌▐▛▀▀▘▐▌ ▝▜▌▐▌ ▐▌ ▝▀▚▖
        ▐▌  ▐▌▐▙▄▄▖▐▌  ▐▌▝▚▄▞▘▗▄▄▞▘

"""

#MENÚ ACCESOS --> LLamo la funció desde acá por requerimiento, los accesos se deben desarrollar de manera modularizada!

def menuAccesos():
    print("\n1 -> Mostrar Accesos")
    print("2 -> Mostrar Intentos Fallidos")
    print(f"{RED}\n3 -> Regresar{RESET}")
    print("...........")

    userOp = int(input("Opción: "))

    match userOp:
        case 1:
            mostrarAccesos()
            menuAccesos()
        case 2:
            mostrarLogs()
            menuAccesos()
        case _:
            exit