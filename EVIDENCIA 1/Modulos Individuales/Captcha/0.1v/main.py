from captcha import generar_operacion

def main():
    num1, operacion, num2 = generar_operacion() # --> importamos lo que genera el captcha
    
    solucion = eval(f'{num1} {operacion} {num2}') # --> calculamos la solución
    
    print(f'¿Cuál es el resultado de {num1} {operacion} {num2}?') 
    
    resultado_usuario = input('Ingrese su respuesta: ') # --> Solicitamos el resultado 
    

    # Calcula el resultado correcto
    try:
        resultado_usuario = float(resultado_usuario)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    
    # Verifica si la respuesta del usuario es correcta
    if resultado_usuario == solucion:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. La respuesta correcta es {solucion}.")

if __name__ == "__main__":
    main()
