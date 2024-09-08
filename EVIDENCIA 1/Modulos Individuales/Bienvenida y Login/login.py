main.py

def main():
       usuarios = {
        'usuario1': 'clave1',
        'usuario2': 'clave2'
    }

    print("¡Bienvenido a INSTATURNO!")

    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuarios.get(usuario) == clave:
        print("Acceso concedido")
    else:
        print("Usuario o clave incorrectos")

    if __name__ == "__main__":
    main()
