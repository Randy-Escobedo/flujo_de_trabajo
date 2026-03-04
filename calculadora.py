# Raiz cuadrada
import math

def sqrt(x):
    if x < 0:
        raise ValueError("No se puede sacar raiz de un numero negativo")
    return math.sqrt(x)