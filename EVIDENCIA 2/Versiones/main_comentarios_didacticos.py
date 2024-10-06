import sys        #importa el módulo sys con funciones del sistema
import os         #importa el módulo os con funciones para manipular archivos y directorios


# Se agregan las rutas de los cuatro directorios al sistema de búsqueda de directorios de Python.
# Esto permite que se importen módulos o paquetes incluidos en ellos sin necesidad de escribir la ruta completa

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Login")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Registro")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Captcha")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Menu")))


from Login import login
from Menu import menu

# define la función principal según los pasos indicados.
def main():
    acceso_id = login()  # Llamar a login y obtener el acceso_id

    if acceso_id:
        menu(acceso_id)  # Pasar el 'acceso_id' al menú
    else:
        print("Error de autenticación. Fin del programa.")

if __name__ == "__main__":
    main()