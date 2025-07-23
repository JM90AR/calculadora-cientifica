"""
Módulo de saludos y conversión de números a palabras.
"""

def saludo_inicial():
    """Muestra un mensaje de bienvenida."""
    print("¡Hola! Bienvenido a la calculadora científica.")


def resultado_palabras(resultado):
    """
    Convierte el resultado numérico a palabras para valores del 0 al 10.
    
    Args:
        resultado: Número a convertir
        
    Returns:
        str: Representación en palabras o mensaje alternativo
    """
    numeros_a_palabras = {
        0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
        6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez"
    }
    
    if resultado in numeros_a_palabras:
        return numeros_a_palabras[resultado]
    else:
        return "número grande o no disponible en palabras"