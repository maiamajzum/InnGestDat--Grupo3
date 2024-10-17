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
