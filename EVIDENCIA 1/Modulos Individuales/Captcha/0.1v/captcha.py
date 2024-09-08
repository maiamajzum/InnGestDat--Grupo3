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
