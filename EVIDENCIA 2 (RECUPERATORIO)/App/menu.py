def menu():

    print("    __  ___ ______ _   __ __  __")
    print("   /  |/  // ____// | / // / / /")
    print("  / /|_/ // __/  /  |/ // / / / ")
    print(" / /  / // /___ / /|  // /_/ /  ")
    print("/_/  /_//_____//_/ |_/ \____/   \n")

    print("SELECIONE:\n")

    print("1 -> Crear Usuario")
    print("2 -> Ingresar")
    print("3 -> Modificar Usuario")
    print("4 -> Eliminar Usuario")
    print("5 -> Buscar Usuario")
    print("6 -> Mostrar todos los usuarios")
    print("0 ->Salir")

    userOp = int(input("SELECCIÓN: "))

    match userOp:
        case 1:
            create_user()
            menu()
        case 2:
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
            menu()


def create_user():

    print("- CREAR USUARIO -")

    userID = int(input("Ingrese el ID: "))
    userName = input("Ingrese NOMBRE: ")
    userPassword = input("Ingrese PASSWORD: ")
    userEmail = input("Ingrese CORREO ELECTRONICO: ")


menu()