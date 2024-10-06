import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Login")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Registro")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Captcha")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Menu")))


from Login import login
from Menu import menu

def main():
    acceso_id = login()  # Llamar a login y obtener el acceso_id

    if acceso_id:
        menu(acceso_id)  # Pasar el 'acceso_id' al menú
    else:
        print("Error de autenticación. Fin del programa.")

if __name__ == "__main__":
    main()