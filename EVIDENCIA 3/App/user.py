import pickle
import os
from datetime import datetime

# - CLASS -> USUARIO -
class Usuario:
    __userID: int
    __userName: str
    __userPassword: str
    __userEmail: str

    # - CONSTRUCTOR -
    def __init__(self, userID: int, userName: str, userPassword: str, userEmail: str):
        self.__userID = userID
        self.__userName = userName
        self.__userPassword = userPassword
        self.__userEmail = userEmail

    # - GET -
    def getId(self) -> int:
        return self.__userID

    def getUsername(self) -> str:
        return self.__userName

    def getPassword(self) -> str:
        return self.__userPassword

    def getEmail(self) -> str:
        return self.__userEmail

    # - SET -
    def setUserName(self, userName: str) -> None:
        self.__userName = userName

    def setUserPassword(self, userPassword: str) -> None:
        self.__userPassword = userPassword

    def setEmail(self, userEmail: str) -> None:
        self.__userEmail = userEmail

    def __str__(self) -> str:
        return f"ID: {self.__userID}, Nombre de Usuario: {self.__userName}, Email: {self.__userEmail}"


# - CLASS -> ACCESO -
class Acceso:
    __id: int
    __fechaIngreso: str
    __fechaSalida: str
    __usuarioLogueado: str

    # - CONSTRUCTOR -
    def __init__(self, id: int, fechaIngreso: str, fechaSalida: str, usuarioLogueado: str):
        self.__id = id
        self.__fechaIngreso = fechaIngreso
        self.__fechaSalida = fechaSalida
        self.__usuarioLogueado = usuarioLogueado

    # - GET -
    def getId(self) -> int:
        return self.__id

    def getFechaIngreso(self) -> str:
        return self.__fechaIngreso

    def getFechaSalida(self) -> str:
        return self.__fechaSalida

    def getUsuarioLogueado(self) -> str:
        return self.__usuarioLogueado

    # - SET -
    def setFechaIngreso(self, fechaIngreso: str) -> None:
        self.__fechaIngreso = fechaIngreso

    def setFechaSalida(self, fechaSalida: str) -> None:
        self.__fechaSalida = fechaSalida

    def setUsuarioLogueado(self, usuarioLogueado: str) -> None:
        self.__usuarioLogueado = usuarioLogueado

    def __str__(self) -> str:
        return f"ID: {self.__id} - Usuario: {self.__usuarioLogueado} - Fecha de Ingreso: {self.__fechaIngreso} - Fecha de Egreso: {self.__fechaSalida}"


# --> MÉTODOS <--


def readUser(archivo="usuarios.ispc"):
    try:
        with open(archivo, "rb") as archivo_binario:
            usuarios = pickle.load(archivo_binario)
    except (FileNotFoundError, EOFError):
        usuarios = []
    return usuarios


def addUser(usuario: Usuario, archivo="usuarios.ispc"):
    try:
        usuariosEnLista = readUser(archivo)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    usuariosEnLista.append(usuario)

    with open(archivo, 'wb') as archivo_binario:
        pickle.dump(usuariosEnLista, archivo_binario)

    print(f"\nEl USUARIO: {usuario.getUsername()} ha sido agregado.")


def showUser(archivo='usuarios.ispc'):
    try:
        usuarios_lista = readUser(archivo)
        for usuario in usuarios_lista:
            print(usuario)
    except FileNotFoundError:
        print("No se encontraron usuarios.")


def updateUser(userID: int, newUserName: str, newPassword: str, newEmail: str, archivo="usuarios.ispc"):
    usuarios_lista = readUser(archivo)

    for usuario in usuarios_lista:
        if usuario.getId() == userID:
            usuario.setUserName(newUserName)
            usuario.setUserPassword(newPassword)
            usuario.setEmail(newEmail)

            with open(archivo, 'wb') as archivo_binario:
                pickle.dump(usuarios_lista, archivo_binario)

            print(f"\nUsuario con ID {userID} ha sido actualizado: {usuario.__str__()}.")
            return

    print(f"\nUsuario con ID {userID} no encontrado.")


# -- CAMBIO MAYOR --

""" 
    Qué cambió? Para no perder la funcionalidad original (buscar por ID) modificamos los parametros que recibe la función
    Ahora, te permite elegir si queres por ID o por NOMBRE

    POR NOMBRE --> controla si está ordenado o no y aplica los criterios de busqueda de la EVIDENCIA 3!!!
"""

def findUser(userOp: int, archivo='usuarios.ispc'):
    usuarios_lista = readUser(archivo)

    if userOp == 1:

        valor = int(input("\nIngrese ID del USUARIO a BUSCAR: "))
        # Búsqueda por ID
        for usuario in usuarios_lista:
            if usuario.getId() == valor:
                print(f"Usuario encontrado: {usuario}")
                return usuario
        print(f"Usuario con ID {valor} no encontrado.")
    
    elif userOp == 2:

        valor = input("\nIngrese NOMBRE del USUARIO a BUSCAR: ")
        # Verificamos --> lista ordenada
        ordenada = all(usuarios_lista[i].getUsername() <= usuarios_lista[i + 1].getUsername() for i in range(len(usuarios_lista) - 1))

        if ordenada: # Técnica de búsqueda BINARIA
            
            izquierda, derecha = 0, len(usuarios_lista) - 1

            while izquierda <= derecha:
                medio = (izquierda + derecha) // 2
                usuario_medio = usuarios_lista[medio].getUsername()

                if usuario_medio == valor:
                    print(f"\nUsuario encontrado mediante Metodo BINARIO: \n{usuarios_lista[medio]}")
                    return usuarios_lista[medio]
                elif usuario_medio < valor:
                    izquierda = medio + 1
                else:
                    derecha = medio - 1

            print(f"\nUsuario con nombre de usuario '{valor}' no encontrado.")

        else:  #Técnica de búsqueda SECUENCIALn
            
            for usuario in usuarios_lista:
                if usuario.getUsername() == valor:
                    print(f"\nUsuario encontrado mediante Metodo SECUENCAIL: \n{usuario}")
                    return usuario
            print(f"\nUsuario con nombre de usuario '{valor}' no encontrado.")

    else:
        print("Parámetro de búsqueda no válido. Utiliza 1 para buscar por ID o 2 para buscar por Username.")



def deleteUser(id, archivo='usuarios.ispc'):
    usuarios_lista = readUser(archivo)

    usuarios_filtrados = [usuario for usuario in usuarios_lista if usuario.getId() != id]

    with open(archivo, 'wb') as archivo_binario:
        pickle.dump(usuarios_filtrados, archivo_binario)

    print(f"Usuario con ID {id} eliminado.")


def ingreso(userName: str, userPassword: str, archivo="usuarios.ispc"):

    usuarios_lista = readUser(archivo)

    for usuario in usuarios_lista:
        if usuario.getUsername() == userName and usuario.getPassword() == userPassword:
            print(f"\n¡Hola, {userName}! Bienvenido/a.")
            print("    ____   ____ ______ _   __ _    __ ______ _   __ ____ ____   ____  ")
            print("   / __ ) /  _// ____// | / /| |  / // ____// | / //  _// __ \ / __ \ ")
            print("  / __  | / / / __/  /  |/ / | | / // __/  /  |/ / / / / / / // / / / ")
            print(" / /_/ /_/ / / /___ / /|  /  | |/ // /___ / /|  /_/ / / /_/ // /_/ /  ")
            print("/_____//___//_____//_/ |_/   |___//_____//_/ |_//___//_____/ \____/   ")
            print("                                                                     ")

            logs(userName)
            return

    # Corregido! había que sacarlo del bucle
    print("\nNombre de usuario o contraseña incorrectos.")
    logs("Ingreso Fallido")

def logs(userName: str, archivo_log="logs.txt"):
    
    if not os.path.exists(archivo_log):
        with open(archivo_log, 'w') as archivo:
            archivo.write("Registro de ingresos de usuarios\n")
            archivo.write("---------------------------------\n")
    
    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Guarda -> user y fecha
    with open(archivo_log, 'a') as archivo:
        archivo.write(f"Usuario: {userName} - Fecha y hora: {fecha_hora_actual}\n")



""" FUNCIONES DE ORDEN --> EVIDENCIA 3 """


def ordenBurbuja(archivo="usuarios.ispc"):
    usuarios = readUser(archivo)

    # Algoritmo BURBUJA °o°
    for i in range(len(usuarios)):
        for j in range(0, len(usuarios)-i-1):
            if usuarios[j].getUsername() > usuarios[j+1].getUsername():
                usuarios[j], usuarios[j+1] = usuarios[j+1], usuarios[j]


    with open(archivo, 'wb') as archivo: #Guarda todo ordenado!
        pickle.dump(usuarios, archivo)

    print("Usuarios ordenados por el método BURBUJA.")
    showUser() #reciclandooo

def ordenSort(archivo="usuarios.ispc"):
    usuarios = readUser(archivo)

    usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario.getUsername())

    with open(archivo, 'wb') as archivo_binario:
        pickle.dump(usuarios_ordenados, archivo_binario)

    print("Usuarios ordenados por el método SORT.")
    showUser(archivo)
