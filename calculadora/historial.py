"""
Módulo para guardar el historial de operaciones.
"""

def guardar_historial(num1, num2, resultado, operacion):
    """
    Guarda la operación realizada en un archivo de historial.
    
    Args:
        num1: Primer operando
        num2: Segundo operando
        resultado: Resultado de la operación
        operacion: Código de la operación (1-4)
    """
    operaciones = {
        "1": "Suma",
        "2": "Resta",
        "3": "Multiplicación",
        "4": "División"
    }
    
    operacion_texto = operaciones.get(operacion, "Operación desconocida")
    
    with open("historial.txt", "a") as file:
        file.write(f"{operacion_texto}: {num1} y {num2} = {resultado}\n")
        
    print("Operación guardada en el historial.")