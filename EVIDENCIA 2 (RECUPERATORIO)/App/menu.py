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
            menu()
        case 2:
            create_user()
            menu()
        case 3:
            menu()
        case 4:
            menu()
        case 5:
            menu()
        case 6:
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