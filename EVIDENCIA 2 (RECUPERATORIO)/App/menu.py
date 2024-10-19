from user import *

def menu():

    print("    __  ___ ______ _   __ __  __")
    print("   /  |/  // ____// | / // / / /")
    print("  / /|_/ // __/  /  |/ // / / / ")
    print(" / /  / // /___ / /|  // /_/ /  ")
    print("/_/  /_//_____//_/ |_/ \____/   \n")

    print("SELECIONE:\n")

    print("1 -> Ingresar")
    print("2 -> Crear Usuario")
    print("3 -> Modificar Usuario")
    print("4 -> Eliminar Usuario")
    print("5 -> Buscar Usuario")
    print("6 -> Mostrar todos los usuarios")
    print("0 ->Salir")

    userOp = int(input("SELECCIÓN: "))

    match userOp:
        case 1:
            ingreso()
            menu()
        case 2:
            print("CREANDO USUARIO:")
            userID, userName, userPassword, userEmail = create_user()
            newUser = Usuario(userID, userName, userPassword, userEmail)
            addUser(newUser)
            print("Usuario AGREGADO.")
            menu()
        case 3:
            print("MODIFICANDO USUARIO:")
            userID = int(input("ingrese ID del USUARIO a MODIFICAR: "))
            updateUser(userID)
            menu()
        case 4:
            print("ELIMINANDO USUARIO:")
            userID = int(input("ingrese ID del USUARIO a MODIFICAR: "))
            deleteUser(userID)
            menu()
        case 5:
            print("BUSCNADO USUARIO:")
            userID = int(input("ingrese ID del USUARIO a MODIFICAR: "))
            userFinded = findUser(userID)
            if userFinded:
                print(f"USUARIO ENCONTRADO -> {userFinded}")
            else:
                print("NO SE ENCONTRÓ.")
            menu()
        case 6:
            print("MOSTRAR TODO: ")
            showUser()
            menu()
        case 0:
            exit
        case _:
            print("Ingrese una OPCIÓN VÁLIDA")
            menu()


def create_user():

    print("- CREAR USUARIO -")

    userID = int(input("Ingrese el ID: "))
    userName = input("Ingrese NOMBRE: ")
    userPassword = input("Ingrese PASSWORD: ")
    userEmail = input("Ingrese CORREO ELECTRONICO: ")


menu()