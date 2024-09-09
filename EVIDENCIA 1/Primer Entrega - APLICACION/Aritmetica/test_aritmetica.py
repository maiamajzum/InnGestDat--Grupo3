# test_aritmetica.py

from aritmetica import (
    sumar,
    restar,
    dividir,
    multiplicar,
    sumar_n,
    promedio_n
)

def test_sumar():
    # Prueba con números positivos
    assert sumar(2.5, 3.5) == 6.0, "Suma de 2.5 y 3.5 debe ser 6.0"
    # Prueba con números negativos
    assert sumar(-1.0, -2.0) == -3.0, "Suma de -1.0 y -2.0 debe ser -3.0"
    # Prueba con cero
    assert sumar(0.0, 5.5) == 5.5, "Suma de 0.0 y 5.5 debe ser 5.5"

def test_restar():
    # Prueba con números positivos
    assert restar(5.5, 2.5) == 3.0, "Resta de 5.5 y 2.5 debe ser 3.0"
    # Prueba con números negativos
    assert restar(-3.0, -2.0) == -1.0, "Resta de -3.0 y -2.0 debe ser -1.0"
    # Prueba con resultado negativo
    assert restar(2.0, 5.0) == -3.0, "Resta de 2.0 y 5.0 debe ser -3.0"

def test_dividir():
    # Prueba con división normal
    assert dividir(10.0, 2.0) == 5.0, "División de 10.0 entre 2.0 debe ser 5.0"
    # Prueba con decimales
    assert dividir(7.5, 2.5) == 3.0, "División de 7.5 entre 2.5 debe ser 3.0"
    # Prueba con división por cero
    try:
        dividir(5.0, 0.0)
        assert False, "División por cero debería lanzar una excepción"
    except ZeroDivisionError:
        assert True

def test_multiplicar():
    # Prueba con números positivos
    assert multiplicar(3.0, 4.0) == 12.0, "Multiplicación de 3.0 y 4.0 debe ser 12.0"
    # Prueba con un número negativo
    assert multiplicar(-2.0, 5.0) == -10.0, "Multiplicación de -2.0 y 5.0 debe ser -10.0"
    # Prueba con cero
    assert multiplicar(0.0, 100.0) == 0.0, "Multiplicación de 0.0 y 100.0 debe ser 0.0"

def test_sumar_n():
    # Prueba con múltiples números positivos
    assert sumar_n(1.0, 2.0, 3.0, 4.0) == 10.0, "Suma de 1.0, 2.0, 3.0, 4.0 debe ser 10.0"
    # Prueba con números mixtos
    assert sumar_n(-1.0, 2.5, -3.5) == -2.0, "Suma de -1.0, 2.5, -3.5 debe ser -2.0"
    # Prueba con un solo número
    assert sumar_n(5.0) == 5.0, "Suma de un solo número 5.0 debe ser 5.0"

def test_promedio_n():
    # Prueba con múltiples números positivos
    assert promedio_n(2.0, 4.0, 6.0, 8.0) == 5.0, "Promedio de 2.0, 4.0, 6.0, 8.0 debe ser 5.0"
    # Prueba con números mixtos
    assert promedio_n(-2.0, 4.0, -6.0, 8.0) == 1.0, "Promedio de -2.0, 4.0, -6.0, 8.0 debe ser 1.0"
    # Prueba con un solo número
    assert promedio_n(10.0) == 10.0, "Promedio de un solo número 10.0 debe ser 10.0"

if __name__ == "__main__":
    test_sumar()
    print("test_sumar pasó todas las pruebas.")
    
    test_restar()
    print("test_restar pasó todas las pruebas.")
    
    test_dividir()
    print("test_dividir pasó todas las pruebas.")
    
    test_multiplicar()
    print("test_multiplicar pasó todas las pruebas.")
    
    test_sumar_n()
    print("test_sumar_n pasó todas las pruebas.")
    
    test_promedio_n()
    print("test_promedio_n pasó todas las pruebas.")
    
    print("Todos los tests han pasado exitosamente.")
