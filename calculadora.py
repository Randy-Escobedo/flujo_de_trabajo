# modulo
def mod(a, b):
    if b == 0:
        raise ValueError("No se puede usar modulo con divisor 0")
    return a % b