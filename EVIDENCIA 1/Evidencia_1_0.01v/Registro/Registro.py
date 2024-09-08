import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Captcha")))
from Captcha import captcha

# Punto 2 de la primera evidencia
# Diccionario para almacenar los usuarios como si fuera base de datos 
usuarios = {}

def longitudCorrecta(nombreUsuario):
    """Verifica que el nombre de usuario tenga entre 6 y 12 caracteres."""
    if len(nombreUsuario) >= 6 and len(nombreUsuario) <= 12:
        return True
    else:
        return False

def contrasenaValida(clave):
    """Verifica que la contraseña cumpla con los requisitos."""
    tieneMinuscula = False
    tieneMayuscula = False
    tieneNumero = False
    tieneCaracterEspecial = False
    
    for caracter in clave:
        if caracter.islower():
            tieneMinuscula = True
        elif caracter.isupper():
            tieneMayuscula = True
        elif caracter.isdigit():
            tieneNumero = True
        else:
            tieneCaracterEspecial = True
    
    if len(clave) >= 8 and tieneMinuscula and tieneMayuscula and tieneNumero and tieneCaracterEspecial:
        return True
    else:
        return False

def correoValido(correo):
    """Verifica que el correo electrónico tenga un formato básico válido."""
    if "@" in correo:
        partes = correo.split("@")
        if len(partes) == 2 and len(partes[0]) > 0 and "." in partes[1] and len(partes[1].split(".")) >= 2:
            return True
    return False
# me quedo largisima esta  parte se podria simplificar hablar con mati
# --> hola, soy Mati... Despues lo veo XDDDD
def fechaValida(fecha):
    """Verifica que la fecha de nacimiento tenga el formato DD/MM/AAAA y sea válida."""
    try:
        dia, mes, año = map(int, fecha.split("/"))
        if mes < 1 or mes > 12:
            return False
        if mes == 2:
            return 1 <= dia <= (29 if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0) else 28)
        return 1 <= dia <= (30 if mes in [4, 6, 9, 11] else 31)
    except ValueError:
        return False

def registrarUsuario():
    while True:
        # Solicitar datos básicos
        print("Vamos a registrar un nuevo usuario.")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        
        # Solicitar y validar DNI
        dni = input("Ingrese su DNI (único): ")
        while dni in usuarios:
            print("El DNI ya está registrado. Intente nuevamente.")
            dni = input("Ingrese su DNI (único): ")
        
        # Solicitar y validar correo electrónico
        correo = input("Ingrese su correo electrónico: ")
        while not correoValido(correo):
            print("El correo electrónico no es válido. Intente nuevamente.")
            correo = input("Ingrese su correo electrónico: ")
        
        # Solicitar y validar fecha de nacimiento
        fechaNacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        while not fechaValida(fechaNacimiento):
            print("La fecha de nacimiento no es válida. Intente nuevamente.")
            fechaNacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        
        # Solicitar y validar nombre de usuario
        nombreUsuario = input("Ingrese su nombre de usuario (6-12 caracteres, único): ")
        
        nombreUsuarioYaExiste = False
        for usuario in usuarios.values():
            if usuario['nombreUsuario'] == nombreUsuario:
                nombreUsuarioYaExiste = True
        
        while not longitudCorrecta(nombreUsuario) or nombreUsuarioYaExiste:
            if not longitudCorrecta(nombreUsuario):
                print("El nombre de usuario debe tener entre 6 y 12 caracteres. Intente nuevamente.")
            if nombreUsuarioYaExiste:
                print("El nombre de usuario ya está en uso. Intente con otro.")
            
            nombreUsuario = input("Ingrese su nombre de usuario (6-12 caracteres, único): ")
            nombreUsuarioYaExiste = False
            for usuario in usuarios.values():
                if usuario['nombreUsuario'] == nombreUsuario:
                    nombreUsuarioYaExiste = True
        
        # Solicitar y validar contraseña
        clave = input("Ingrese su contraseña (mínimo 8 caracteres, con al menos 1 minúscula, 1 mayúscula, 1 número, y 1 carácter especial): ")
        
        while not contrasenaValida(clave):
            print("La contraseña no cumple con los requisitos. Intente nuevamente.")
            clave = input("Ingrese su contraseña: ")


        if captcha():
                
            # Guardar el usuario en la base de datos (diccionario)
            usuarios[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "fechaNacimiento": fechaNacimiento,
            "nombreUsuario": nombreUsuario,
            "clave": clave
            }
            print(f"Usuario {nombreUsuario} registrado con éxito.")
        
        
        
        # Solicitar si se desea registrar otro usuario
        respuesta = input("¿Desea registrar otro usuario? (si/no): ").lower()
        if respuesta != "si":
            break
