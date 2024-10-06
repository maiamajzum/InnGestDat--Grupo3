import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Login")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Registro")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Captcha")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Menu")))


from Login import login
from Registro import registrarUsuario
from Captcha import captcha
from Menu import menu

def main():
    print("Bienvenido.")
    if login():
        #registrarUsuario()
        menu()


if __name__ == "__main__":
    main()

