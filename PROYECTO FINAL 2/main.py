from gestionUsuario import *
from gestionAcceso import *
from gestionPluvial import *
from colores import *
from gestionDB import *

def main():

    # -- MENÚ PRINCIPAL --
    # Desde este menú, vamos a llamar a los menús 

    print("  __  __  ______  _   _    __    _____   _____   _____  _   _   _____  _____  _____          _      ")
    print(" |  \/  ||  ____|| \ | | _/_/_  |  __ \ |  __ \ |_   _|| \ | | / ____||_   _||  __ \  /\    | |     ")
    print(" | \  / || |__   |  \| || | | | | |__) || |__) |  | |  |  \| || |       | |  | |__) |/  \   | |     ")
    print(" | |\/| ||  __|  | . ` || | | | |  ___/ |  _  /   | |  | . ` || |       | |  |  ___// /\ \  | |     ")
    print(" | |  | || |____ | |\  || |_| | | |     | | \ \  _| |_ | |\  || |____  _| |_ | |   / ____ \ | |____ ")
    print(" |_|  |_||______||_| \_| \___/  |_|     |_|  \_\|_____||_| \_| \_____||_____||_|  /_/    \_\|______|")

    print ("\n- Bienvenido -")

    print(f"{GREEN}\n1 -> Menú: Usuario y Accesos{RESET}")
    print(f"{YELLOW}2 -> Ingresar a la Base de Datos{RESET}")
    print(f"{BLUE}3 -> Registros Pluviales{RESET}")
    print(f"\n{RED}4 -> Salir{RESET}")
    print("...........")

    userOp = int(input("Opción: "))

    match userOp:
        case 1:
            menu_user()
        case 2:
            userName = input(f"{YELLOW}NOMBRE: {RESET}")
            userPassword = input(f"{YELLOW}CONTRASEÑA: {RESET}")
            acceso= ingreso(userName, userPassword)

            if acceso:
                menu_principalDB()

        case 3:
            menu_lluvia()
            main()
        case _:
            exit

def menu_user():

    # -- MENÚ USUARIO --
    # Desde este menú, vamos a llamar a Metodos del Modulo Usuario (CRUD y Archivos Binarios)

    print(f"{GREEN}\n")
    print("  __  __  ______  _   _    __    _    _   _____  _    _           _____   _____  ____  ")
    print(" |  \/  ||  ____|| \ | | _/_/_  | |  | | / ____|| |  | |   /\    |  __ \ |_   _|/ __ \ ")
    print(" | \  / || |__   |  \| || | | | | |  | || (___  | |  | |  /  \   | |__) |  | | | |  | |")
    print(" | |\/| ||  __|  | . ` || | | | | |  | | \___ \ | |  | | / /\ \  |  _  /   | | | |  | |")
    print(" | |  | || |____ | |\  || |_| | | |__| | ____) || |__| |/ ____ \ | | \ \  _| |_| |__| |")
    print(f" |_|  |_||______||_| \_| \___/   \____/ |_____/  \____//_/    \_\|_|  \_\|_____|\____/ {RESET}")

    print(f"\n1 -> Menú: CRUD")
    print("2 -> Menú: Datos de Acceso")
    print(f"3 -> Menú: Ordenamiento de Datos")
    print(f"{RED}\n4 -> Regresar{RESET}\n")
    print("...........")

    userOp = int(input("Opción: "))

    # LLamamos a los métodos

    match userOp:
        case 1:
            menuCRUD()
            menu_user()
        case 2:
            menuAccesos()
            menu_user()
        case 3:
            menuOrden()
            menu_user()
        case _:
            print("Regresando al Menú Anterior")
            main()                                                                            
 


main()