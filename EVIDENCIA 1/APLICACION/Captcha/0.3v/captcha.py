import random

def generar_operacion():
    signos = ['+', '-', '*', '/'] # --> array de signos
    operacion = random.choice(signos) # --> selección aleatoria de la operación
    
    num1 = random.randint(1, 10) # --> número aleatorios (valores intercambiables)
    num2 = random.randint(1, 10)
    
    if operacion == '/':
        num2 = random.randint(1, 10)  # <-- para evitar dividir por cero
        while num1 % num2 != 0:
            num1 = random.randint(1, 10)
    
    return num1, operacion, num2 # <-- retornamos para el main

def captcha():

    status = 0
    intentos = 3 # --> Los intentos límitados no eran requerimiento de la "Evidencia 1", se lo agregué yo

    print('Para continuar, conteste:\n')

    while intentos > 0 and status  == 0:
        
        num1, operacion, num2 = generar_operacion()
        solucion = eval(f'{num1} {operacion} {num2}')

        print(f'¿Cuál es el resultado de {num1} {operacion} {num2}?')

        resultado_usuario = input('Ingrese su respuesta: \n')

        intentos -= 1 # --> Siempre consideré que los intentos comienzan a contar desde el primer uso

        try:
            resultado_usuario = float(resultado_usuario)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if resultado_usuario == solucion:
            print("¡Correcto!\n")
            status = 1
        else:
            print(f"Incorrecto. La respuesta correcta es {solucion}.\n")

        # opción de salir antes de tiempo (Requerimeinto de la "Evidencia 1")
            if intentos > 0:
                retry = input('Desea seguir intentando? (Y/N): ').strip().lower() # --> por las dudas, que todo sea minuscula
                if retry != 'y':
                    print('Saliendo...')
                    break

    return status