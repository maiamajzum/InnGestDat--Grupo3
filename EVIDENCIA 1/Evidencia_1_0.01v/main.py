import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Login")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Registro")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Captcha")))
from Login import login
from Registro import registrarUsuario
from Captcha import captcha

def main():
    print("Bienvenido.")
    if login():
        registrarUsuario()


if __name__ == "__main__":
    main()


