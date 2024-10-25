import pickle
import os
import datetime
from clases import *
from colores import *

"""
 
▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▖ ▗▄▄▄  ▗▄▖  ▗▄▄▖
▐▛▚▞▜▌▐▌     █ ▐▌ ▐▌▐▌  █▐▌ ▐▌▐▌   
▐▌  ▐▌▐▛▀▀▘  █ ▐▌ ▐▌▐▌  █▐▌ ▐▌ ▝▀▚▖
▐▌  ▐▌▐▙▄▄▖  █ ▝▚▄▞▘▐▙▄▄▀▝▚▄▞▘▗▄▄▞▘

"""

# Leer usuarios desde archivo binario
def leerUsuario(archivo="usuarios.ispc") -> list:
    try:
        with open(archivo, "rb") as archivo_binario:
            usuarios = pickle.load(archivo_binario)
    except (FileNotFoundError, EOFError):
        usuarios = []
    return usuarios


# Agregar un nuevo usuario
def agregarUsuario(usuario: Usuario, archivo="usuarios.ispc") -> None:
    try:
        usuariosEnLista = leerUsuario(archivo)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    usuariosEnLista.append(usuario)

    with open(archivo, 'wb') as archivo_binario:
        pickle.dump(usuariosEnLista, archivo_binario)

    ordenarUsuarios(1)
    print(f"{GREEN}\nEl USUARIO: {usuario.getUsername()} ha sido agregado.{RESET}")
    


# Mostrar todos los usuarios
def mostrarUsuario(archivo='usuarios.ispc') -> None:

    ordenarUsuarios(1) # Contemplamos la posibilidad de que se realice esto justo despues de buscar por EMAIL

    try:
        usuarios_lista = leerUsuario(archivo)
        if not usuarios_lista:
            print("No se encontraron usuarios.")
        for usuario in usuarios_lista:
            print(usuario)
    except FileNotFoundError:
        print("No se encontraron usuarios.")


# Actualizar un usuario por ID
def actualizarUsuario(userID: int, newUserDNI: int, newUserName: str, newPassword: str, newEmail: str, archivo="usuarios.ispc") -> None:
    usuarios_lista = leerUsuario(archivo)

    for usuario in usuarios_lista:
        if usuario.getId() == userID:
            usuario.setUserDNI(newUserDNI)
            usuario.setUserName(newUserName)
            usuario.setUserPassword(newPassword)
            usuario.setEmail(newEmail)

            with open(archivo, 'wb') as archivo_binario:
                pickle.dump(usuarios_lista, archivo_binario)

            print(f"{GREEN}\nUsuario Número: {userID}, ha sido actualizado:\n {usuario}.{RESET}")
            return

    print(f"\nUsuario con ID {userID} no encontrado.")


# Buscar usuario por DNI o Username


def buscarUsuario(userOp: int, archivo='usuarios.ispc'):
    usuarios_lista = leerUsuario(archivo)


    if userOp == 1:
        # Ordenar usuarios por DNI antes de la búsqueda
        ordenarUsuarios(1)

        # Búsqueda binaria por DNI
        valor = int(input("\nIngrese DNI del USUARIO a BUSCAR: "))
        print(f"{GREEN}Realizando búsqueda por método BINARIO{RESET}")

        izquierda, derecha = 0, len(usuarios_lista) - 1
        log_detalles = f"Búsqueda Binaria por DNI: buscando el DNI {valor} en el archivo '{archivo}' que contiene {len(usuarios_lista)} usuarios.\n"
        intentos = 0

        # Verificación de límites
        if usuarios_lista[izquierda].getDNI() > valor:
            log_detalles += f"No se encuentra registrado el usuario con ese DNI debido a que el DNI a buscar es más chico que el más chico de los registrados.\n"
            generar_log("DNI", log_detalles)
            return None

        if usuarios_lista[derecha].getDNI() < valor:
            log_detalles += f"No se encuentra registrado el usuario con ese DNI debido a que el DNI a buscar es más grande que el más grande de los registrados.\n"
            generar_log("DNI", log_detalles)
            return None

        while izquierda <= derecha:
            intentos += 1
            medio = (izquierda + derecha) // 2
            usuario_medio = usuarios_lista[medio].getDNI()
            log_detalles += f"Intento {intentos}: DNI del usuario de la posición {medio} es {usuario_medio}. "

            if usuario_medio == valor:
                log_detalles += f"Se encontró el usuario en {intentos} intentos.\n"
                generar_log("DNI", log_detalles)
                print(f"{GREEN}Usuario encontrado: {usuarios_lista[medio]}{RESET}")
                return usuarios_lista[medio]
            elif usuario_medio < valor:
                log_detalles += f"Buscando en la subsecuencia de la derecha (DNI más grandes) (posición {medio + 1} a {derecha}).\n"
                izquierda = medio + 1
            else:
                log_detalles += f"Buscando en la subsecuencia de la izquierda (DNI más chicos) (posición {izquierda} a {medio - 1}).\n"
                derecha = medio - 1

        log_detalles += f"Se realizaron {intentos} intentos y no se encontró el DNI buscado, no está registrado.\n"
        generar_log("DNI", log_detalles)
        print(f"DNI no encontrado")

    elif userOp == 2:
        archivo_ordenado = 'usuariosOrdenadosPorUsername.ispc'

        if os.path.exists(archivo_ordenado):
            # Leer usuarios de archivo ordenado y realizar búsqueda binaria por nombre
            usuarios_lista = leerUsuario(archivo_ordenado)
            valor = input("\nIngrese NOMBRE del USUARIO a BUSCAR: ")
            print(f"{GREEN}Realizando búsqueda por método BINARIO{RESET}")

            izquierda, derecha = 0, len(usuarios_lista) - 1
            log_detalles = f"Búsqueda Binaria por NOMBRE: buscando el nombre '{valor}' en el archivo '{archivo_ordenado}' que contiene {len(usuarios_lista)} usuarios.\n"
            intentos = 0

            while izquierda <= derecha:
                intentos += 1
                medio = (izquierda + derecha) // 2
                usuario_medio = usuarios_lista[medio].getUsername()

                log_detalles += f"Intento {intentos}: Nombre del usuario de la posición {medio} es '{usuario_medio}'. "

                if usuario_medio == valor:
                    log_detalles += f"Se encontró el usuario en {intentos} intentos.\n"
                    print(f"{GREEN}Usuario encontrado: {usuarios_lista[medio]}{RESET}")
                    generar_log("NOMBRE", log_detalles)
                    return usuarios_lista[medio]
                elif usuario_medio < valor:
                    izquierda = medio + 1
                else:
                    derecha = medio - 1

        else:
            # Búsqueda secuencial en 'usuarios.ispc'
            valor = input("\nIngrese NOMBRE del USUARIO a BUSCAR: ")
            print(f"{GREEN}Realizando búsqueda por método SECUENCIAL (el archivo 'usuariosOrdenadosPorUsername.ispc' no fue encontrado){RESET}")

            intentos = 0
            for usuario in usuarios_lista:
                intentos += 1
                usuario_medio = usuario.getUsername()
                print(f"Intento {intentos}: buscando el username '{valor}' (comparando con '{usuario_medio}')")

                if usuario_medio == valor:
                    print(f"{GREEN}Usuario encontrado mediante búsqueda secuencial: {usuario}{RESET}")
                    return usuario
            
            print(f"No se encuentra registrado el usuario con nombre '{valor}' en el archivo principal. Se realizaron {intentos} intentos.")

   

            log_detalles += f"Se realizaron {intentos} intentos y no se encontró el nombre buscado, no está registrado.\n"
 
    elif userOp == 3:
        # Ordenar usuarios por email antes de la búsqueda
        ordenarUsuarios(3)

        # Búsqueda binaria por email
        valor = input("\nIngrese EMAIL del USUARIO a BUSCAR: ")
        print(f"{GREEN}Realizando búsqueda por método BINARIO{RESET}")

        izquierda, derecha = 0, len(usuarios_lista) - 1
        log_detalles = f"Búsqueda Binaria por EMAIL: buscando el email '{valor}' en el archivo '{archivo}' que contiene {len(usuarios_lista)} usuarios.\n"
        intentos = 0

        while izquierda <= derecha:
            intentos += 1
            medio = (izquierda + derecha) // 2
            usuario_medio = usuarios_lista[medio].getEmail()
            log_detalles += f"Intento {intentos}: Email del usuario de la posición {medio} es '{usuario_medio}'. \n"

            if usuario_medio == valor:
                log_detalles += f"{GREEN}Se encontró el usuario en {intentos} intentos.\n"
                generar_log("EMAIL", log_detalles)
                print(f"Usuario encontrado: {usuarios_lista[medio]}{RESET}")
                return usuarios_lista[medio]
            elif usuario_medio < valor:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        log_detalles += f"Se realizaron {intentos} intentos y no se encontró el email buscado, no está registrado.\n"
        generar_log("EMAIL", log_detalles)
        print("log_detalles")
            
        print(f"No se encuentra registrado el usuario con nombre '{valor}' en el archivo principal. Se realizaron {intentos} intentos.")

    else:
        print("Parámetro de búsqueda no válido. Utiliza 1 para buscar por DNI, 2 para buscar por nombre, o 3 para buscar por email.")











# Eliminar un usuario por ID
def eliminarUsuario(id: int, archivo='usuarios.ispc') -> None:
    usuarios_lista = leerUsuario(archivo)

    # Filtramos usuarios cuyo ID no sea el proporcionado
    usuarios_filtrados = [usuario for usuario in usuarios_lista if usuario.getId() != id]

    # Si la longitud de la lista no cambia, significa que no se encontró el ID
    if len(usuarios_lista) == len(usuarios_filtrados):
        print(f"Usuario con ID {id} no encontrado.")
    else:
        # Si se encontró y eliminó el usuario, guardamos la lista filtrada
        with open(archivo, 'wb') as archivo_binario:
            pickle.dump(usuarios_filtrados, archivo_binario)

        print(f"{GREEN}Usuario con ID {id} eliminado.{RESET}")


def create_user(archivo="usuarios.ispc"):
    # Leer usuarios existentes
    usuariosEnLista = leerUsuario(archivo)

    # Verificar si hay usuarios en la lista y obtener el ID más grande
    if usuariosEnLista:
        max_id = max(usuario.getId() for usuario in usuariosEnLista)
        userID = max_id + 1
    else:
        userID = 1  # Si no hay usuarios, el primer ID será 1

    print(f"{GREEN}El ID asignado al nuevo usuario es: {userID}{RESET}")
    
    # Solicitar los demás datos del usuario
    userDNI = int(input("Ingrese DNI: "))
    userName = input("Ingrese NOMBRE: ")
    userPassword = input("Ingrese PASSWORD: ")
    userEmail = input("Ingrese CORREO ELECTRONICO: ")

    # Devolver los datos del usuario (incluyendo el nuevo ID)
    return userID, userDNI, userName, userPassword, userEmail


# -- METODOS de ORDENAMIENTO --

def ordenarUsuarios(parametro: int, archivo='usuarios.ispc'):
    usuarios = leerUsuario(archivo)

    if parametro == 1:
        usuarios_ordenados = sorted(usuarios, key= lambda usuario: usuario.getDNI())

        with open(archivo, 'wb') as archivo_binario:
            pickle.dump(usuarios_ordenados, archivo_binario)

        mensaje = "'usuarios.ispc' ordenado por DNI mediante MÉTODO SORT."
        return mensaje
        
    
    elif parametro == 2:
        # Ordenar por nombre de usuario usando el método BURBUJA
        for i in range(len(usuarios)):
            for j in range(0, len(usuarios) - i - 1):
                if usuarios[j].getUsername() > usuarios[j + 1].getUsername():
                    usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]

        # Guardar en un archivo nuevo "usuariosOrdenados.ispc"
        with open("usuariosOrdenadosPorUsername.ispc", 'wb') as archivo_ordenado:
            pickle.dump(usuarios, archivo_ordenado)

        mensaje = "'usuarios.ispc' ordenado por NOMBRE mediante MÉTODO BURBUJA y guardado en 'usuariosOrdenados.ispc'."
        return mensaje
    
    elif parametro == 3:
        usuarios_ordenados = sorted(usuarios, key= lambda usuario: usuario.getEmail())

        with open(archivo, 'wb') as archivo_binario:
            pickle.dump(usuarios_ordenados, archivo_binario)

        mensaje = "'usuarios.ispc' ordenado por EMAIL mediante MÉTODO SORT."
        return mensaje
    
    else:
        return "Parámetro no válido. Utiliza 1 para ordenar por DNI, 2 para ordenar por nombre, o 3 para ordenar por email."
  



# -- Creo la función acá para evitar referencias circulares... ya lo modifico para ver como lo podemos solucionar
def generar_log(nombre_campo, detalles): 
    fecha = datetime.datetime.now().strftime('%Y%m%d')
    # Definir la ruta del archivo de log
    carpeta_destino = 'busquedasYordenamientos'
    archivo_log = os.path.join(carpeta_destino, f"buscandoUsuarioPor{nombre_campo}-{fecha}.txt")

    # Verificar si la carpeta existe, si no, crearla
    os.makedirs(carpeta_destino, exist_ok=True)

    # Escribir el log
    with open(archivo_log, 'a') as log:
        log.write(detalles + '\n')


""" 
    
        ▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖ ▗▄▄▖
        ▐▛▚▞▜▌▐▌   ▐▛▚▖▐▌▐▌ ▐▌▐▌   
        ▐▌  ▐▌▐▛▀▀▘▐▌ ▝▜▌▐▌ ▐▌ ▝▀▚▖
        ▐▌  ▐▌▐▙▄▄▖▐▌  ▐▌▝▚▄▞▘▗▄▄▞▘

"""


# MENÚ CRUD -> El Read está en otro menú, como lo pidieron por consigna!
def menuCRUD():
    
    print(f"\n1 -> Crear Usuario")
    print("2 -> Modificar Usuario")
    print(f"3 -> Eliminar Usuario")
    print(f"{RED}\n4 -> Regresar{RESET}")
    print("...........")

    userOp = int(input("Opción: "))

    match userOp:
        case 1:
            userID, userDNI, userName, userPassword, userEmail = create_user()
            newUser = Usuario(userID, userDNI, userName, userPassword, userEmail)
            agregarUsuario(newUser)
            print("...........")

            menuCRUD()
        case 2:
            userID = int(input("Ingrese el ID del USUARIO a MODIFICAR: "))
            userDNI = int(input("Ingrese el NUEVO DNI: "))
            userName = input("Ingrese el NUEVO NOMBRE: ")
            userPassword = input("Ingrese la NUEVA CONTRASEÑA: ")
            userEmail = input("Ingrese el NUEVO EMAIL: ")
            actualizarUsuario(userID, userDNI, userName, userPassword, userEmail)
            print("...........")

            menuCRUD()
        case 3:
            userID = int(input("Ingrese el ID del USUARIO a ELIMINAR: "))
            eliminarUsuario(userID)
            print("...........")

            menuCRUD()
        case 4:
            print("Regresando al Menú Anterior")
            exit
        case _:
            print("Regresando al Menú Anterior")
            exit

def menuOrden():

    print("\n1 -> ORDENAR Usuarios por NOMBRE")
    print("2 -> Buscar Usuario por DNI")
    print("3 -> Buscar Usuario por NOMBRE")
    print("4 -> Buscar Usuario por EMAIL")
    print("5 -> Mostrar TODO")
    print(f"{RED}\n6 -> Regresar{RESET}")
    print("...........")

    userOp = int(input("Opción: "))

    match userOp:
        case 1:
            mensaje = ordenarUsuarios(2)
            print(mensaje)
            menuOrden()
        case 2:
            buscarUsuario(1)
            menuOrden()
        case 3:
            buscarUsuario(2)
            menuOrden()
        case 4:
            buscarUsuario(3)
            menuOrden()
        case 5:
            print("\n 1 -> Mostrar 'usuarios.ispc'")
            print(" 2 -> Mostrar 'usuariosOrdenadosPorUsername.ispc'")
            print(f"{RED}Regresar{RESET}")
            print("...........")
            userOp = int(input("Opción: "))
            match userOp:
                case 1:
                    mostrarUsuario()
                    menuOrden()
                case 2:
                    mostrarUsuario("usuariosOrdenadosPorUsername.ispc")
                    menuOrden()
                case _:
                    exit
        case _:
            exit