def login():
    usuarios = {
        'usuario1': 'clave1',
        'usuario2': 'clave2'
    }

    print("¡Bienvenido a INSTATURNO!")

    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuarios.get(usuario) == clave:
        print("Acceso concedido")
        print("\n")
        return True
    

    else:
        print("Usuario o clave incorrectos")
        print("\n")
        return False

