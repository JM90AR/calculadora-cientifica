import math

# Funciones para la interfaz gráfica (nuevas)
def calcular_raiz(num):
    """Calcula la raíz cuadrada de un número"""
    try:
        return round(math.sqrt(num), 4)
    except ValueError:
        return "Error: Número negativo"

def calcular_seno(num):
    """Calcula el seno de un ángulo en grados"""
    return round(math.sin(math.radians(num)), 4)

def calcular_coseno(num):
    """Calcula el coseno de un ángulo en grados"""
    return round(math.cos(math.radians(num)), 4)

def calcular_log(num):
    """Calcula el logaritmo natural"""
    try:
        return round(math.log(num), 4) if num > 0 else "Error: Número ≤ 0"
    except ValueError:
        return "Error: Número inválido"

# Función original (conservada para compatibilidad)
def calculadora_cientifica():
    print("\nOpciones científicas: 1) Raíz cuadrada 2) Seno 3) Coseno 4) Logaritmo")
    opcion = input("Elige una opción científica: ")
    
    try:
        numero = float(input("Introduce un número: "))
        
        if opcion == "1":
            resultado = calcular_raiz(numero)
            print(f'Raíz cuadrada: {resultado}')
        elif opcion == "2":
            resultado = calcular_seno(numero)
            print(f'Seno: {resultado}')
        elif opcion == "3": 
            resultado = calcular_coseno(numero)
            print(f'Coseno: {resultado}')
        elif opcion == "4":
            resultado = calcular_log(numero)
            print(f'Logaritmo: {resultado}')
        else:
            print("Opción no válida.")
            
    except ValueError:
        print("Error: Introduce un número válido.")