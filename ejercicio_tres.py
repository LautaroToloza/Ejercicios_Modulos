"""
3. Calcular el factorial de un numero ingresado por teclado. Utilizar la
función del módulo math. Debe utilizar SOLO esa función. La
función factorial necesita como parámetro un numero entero.
"""
from Modulos import calcular_factorial


def test():
    num = int(input("Ingrese el número a calcular el factorial: "))
    resultado = calcular_factorial(num)
    print(f"El factorial de '{num}' es: {resultado}")


if __name__ == "__main__":
    test()
