
# División
def div(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    return a / b


# Potencia
def power(a, b):
    return a ** b


# modulo
def mod(a, b):
    if b == 0:
        raise ValueError("No se puede usar modulo con divisor 0")
    return a % b


# Raiz cuadrada
import math

def sqrt(x):
    if x < 0:
        raise ValueError("No se puede sacar raiz de un numero negativo")
    return math.sqrt(x)

# Porcentaje
def percent(value, pct):
    return value * (pct / 100)