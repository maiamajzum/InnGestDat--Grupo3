import random

def generar_operacion():
    signos = ['+', '-', '*', '/'] # --> array de signos
    operacion = random.choice(signos) # --> selección aleatoria de la operación
    
    num1 = round(random.uniform(1, 10), 2) # .uniform --> número aleatorios con 2 decimales (Requerimiento)
    num2 = round(random.uniform(1, 10), 2)
    
    if operacion == '/':
        while num2 == 0:  # <-- Para evitar dividir por cero
            num2 = round(random.uniform(1, 10), 2)
        while num1 % num2 != 0: # <-- Asegurarse de que num1 sea divisible por num2
            num1 = round(random.uniform(1, 10), 2)
    
    return num1, operacion, num2 # <-- retornamos para el main

def captcha():

    status = 0
    intentos = 3 # --> Los intentos límitados no eran requerimiento de la "Evidencia 1", se lo agregué yo

    print('Para continuar, conteste:\n')

    while intentos > 0 and status  == 0:
        
        num1, operacion, num2 = generar_operacion()
        solucion = round(eval(f'{num1} {operacion} {num2}'), 2)

        print(f'¿Cuál es el resultado de {round(num1, 2)} {operacion} {round(num2, 2)}?')

        resultado_usuario = input('Ingrese su respuesta(con 2 DECIMALES): \n')

        intentos -= 1 # --> Siempre consideré que los intentos comienzan a contar desde el primer uso

        try:
            resultado_usuario = float(resultado_usuario)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if round(resultado_usuario, 2) == solucion:
            print("¡Correcto!\n")
            status = 1
        else:
            print(f"Incorrecto. La respuesta correcta es {round(solucion, 2)}.\n")

        # opción de salir antes de tiempo (Requerimeinto de la "Evidencia 1")
            if intentos > 0:
                retry = input('Desea seguir intentando? (Y/N): ').strip().lower() # --> por las dudas, que todo sea minuscula
                if retry != 'y':
                    print('Saliendo...')
                    break

    return status