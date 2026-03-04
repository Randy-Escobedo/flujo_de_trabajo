from calculadora import *

def mostrar_menu():
    print("\n--- CALCULADORA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Porcentaje")
    print("8. Valor absoluto")
    print("9. Modulo")
    print("0. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    try:
        if opcion == "1":
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("Resultado:", add(a, b))

        elif opcion == "2":
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("Resultado:", sub(a, b))

        elif opcion == "3":
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("Resultado:", mul(a, b))

        elif opcion == "4":
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("Resultado:", div(a, b))

        elif opcion == "5":
            a = float(input("Base: "))
            b = float(input("Exponente: "))
            print("Resultado:", power(a, b))

        elif opcion == "6":
            x = float(input("Numero: "))
            print("Resultado:", sqrt(x))

        elif opcion == "7":
            valor = float(input("Numero base: "))
            pct = float(input("Porcentaje: "))
            print("Resultado:", percent(valor, pct))

        elif opcion == "8":
            x = float(input("Numero: "))
            print("Resultado:", absolute(x))

        elif opcion == "9":
            a = float(input("Numero: "))
            b = float(input("Divisor: "))
            print("Resultado:", mod(a, b))

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opcion no valida")

    except Exception as e:
        print("Error:", e)