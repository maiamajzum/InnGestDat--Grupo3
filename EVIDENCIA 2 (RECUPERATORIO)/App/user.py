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
        with open(archivo, "rb") as archivo:
            usuarios = pickle.load(archivo)
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

    with open(archivo, 'wb') as archivo:
        pickle.dump(usuariosEnLista, archivo) 

    print(f"El USUARIO: {usuario.getUsername()} ha sido agregado.")


def showUser(archivo='usuarios.ispc'): 
    try:
        usuarios_lista = readUser(archivo)
        for usuario in usuarios_lista:
            print(usuario)
    except FileNotFoundError:
        print("No se encontraron usuarios.")


def updateUser(username: str, password: str, email: str, archivo="usuarios.ispc"):
    usuarios_lista = readUser(archivo)

    for usuario in usuarios_lista:
        if usuario.getUsername() == username:
            usuario.setUserName(username)
            usuario.setUserPassword(password)
            usuario.setEmail(email)
            
            with open(archivo, 'wb') as archivo:
                pickle.dump(usuarios_lista, archivo)
            print(f"Usuario con datos actualizados: {usuario.__str__()}.")
            return
    print(f"Usuario con nombre de usuario '{username}' no encontrado.")


def findUser(id_usuario, archivo='usuarios.ispc'):
    usuarios_lista = readUser(archivo)
    for usuario in usuarios_lista:
        if usuario.getId() == id_usuario:
            return usuario
    return None


def deleteUser(id, archivo='usuarios.ispc'):
    usuarios_lista = readUser(archivo)

    usuarios_filtrados = [usuario for usuario in usuarios_lista if usuario.getId() != id]

    with open(archivo, 'wb') as archivo:
        pickle.dump(usuarios_filtrados, archivo)

    print(f"Usuario con ID {id} eliminado.")


def ingreso():
    print("    ____   ____ ______ _   __ _    __ ______ _   __ ____ ____   ____  ")
    print("   / __ ) /  _// ____// | / /| |  / // ____// | / //  _// __ \ / __ \ ")
    print("  / __  | / / / __/  /  |/ / | | / // __/  /  |/ / / / / / / // / / / ")
    print(" / /_/ /_/ / / /___ / /|  /  | |/ // /___ / /|  /_/ / / /_/ // /_/ /  ")
    print("/_____//___//_____//_/ |_/   |___//_____//_/ |_//___//_____/ \____/   ")
    print("                                                                     ")