"""
4. Cree un modulo que implemente dos funciones, una que retorne el
mayor de tres números enteros y otra que retorne el menor de los
tres. El módulo principal es el encargado de importar al modulo
anteriormente mencionado, de permitir la carga de los tres números
enteros que se deben pasar como parámetros a las funciones y de
mostrar los resultados de las mismas.
"""
from Modulos import mayor_numero, menor_numero


def test():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    n3 = int(input("Ingrese el tercer número: "))
    may = mayor_numero(n1, n2, n3)
    men = menor_numero(n1, n2, n3)
    print("---" * 25)
    print(f"El mayor número fue: {may}")
    print(f"El menor número fue: {men}")
    print("---" * 25)


if __name__ == "__main__":
    test()
