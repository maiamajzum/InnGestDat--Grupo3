import pickle

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

    print(f"El USUARIO: {usuario.getUsername()} ha sido agregado.")


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

            print(f"Usuario con ID {userID} ha sido actualizado: {usuario.__str__()}.")
            return

    print(f"Usuario con ID {userID} no encontrado.")


def findUser(id_usuario, archivo='usuarios.ispc'):
    usuarios_lista = readUser(archivo)
    for usuario in usuarios_lista:
        if usuario.getId() == id_usuario:
            return usuario
    return None


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
            print(f"¡Hola, {userName}! Bienvenido/a.")

            print("    ____   ____ ______ _   __ _    __ ______ _   __ ____ ____   ____  ")
            print("   / __ ) /  _// ____// | / /| |  / // ____// | / //  _// __ \ / __ \ ")
            print("  / __  | / / / __/  /  |/ / | | / // __/  /  |/ / / / / / / // / / / ")
            print(" / /_/ /_/ / / /___ / /|  /  | |/ // /___ / /|  /_/ / / /_/ // /_/ /  ")
            print("/_____//___//_____//_/ |_/   |___//_____//_/ |_//___//_____/ \____/   ")
            print("                                                                     ")

            return
        else:
            print("Nombre de usuario o contraseña incorrectos.")


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
