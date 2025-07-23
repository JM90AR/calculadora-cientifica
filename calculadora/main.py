"""
Módulo principal de la calculadora científica.

Este módulo proporciona la interfaz principal y coordina
las operaciones básicas y científicas.
"""

from calculadora.saludo import saludo_inicial, resultado_palabras
from calculadora.cientifica import calculadora_cientifica
from calculadora.historial import guardar_historial


def sumar(a, b):
    """Realiza la suma de dos números."""
    return a + b


def restar(a, b):
    """Realiza la resta de dos números."""
    return a - b


def multiplicar(a, b):
    """Realiza la multiplicación de dos números."""
    return a * b


def dividir(a, b):
    """Realiza la división de dos números con manejo de división por cero."""
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


def calculadora():
    """Función principal que maneja el flujo de la calculadora."""
    saludo_inicial()
    
    while True:
        print("\nOperaciones disponibles:")
        print("1) Sumar")
        print("2) Restar") 
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Modo científico")
        print("6) Salir")
        
        opcion = input("\nElige una operación: ")
        
        if opcion == "6":
            print("¡Hasta luego!")
            break
        
        if opcion == "5":
            calculadora_cientifica()
            continue
        
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            
            if opcion == "1":
                resultado = sumar(num1, num2)
            elif opcion == "2":
                resultado = restar(num1, num2)
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
            elif opcion == "4":
                resultado = dividir(num1, num2)
            else:
                print("Opción no válida.")
                continue
            
            resultado_en_palabras = resultado_palabras(resultado)
            print(f"\nResultado: {resultado} ({resultado_en_palabras})")
            
            guardar_historial(num1, num2, resultado, opcion)
            
        except ValueError:
            print("Error: Introduce un número válido.")


if __name__ == "__main__":
    calculadora()