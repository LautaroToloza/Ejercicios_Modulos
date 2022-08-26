"""
5. Desarrolle un programa que trabaje con módulos. El módulo que
debe crear debe tener una función que tome dos valores numéricos
(uno inicial y otro final). El programa debe leer una n cantidad de
números que indique el usuario y debe controlar que dicho número
se encuentre entre los valores de inicial y final ingresados
anteriormente. La función retornará el valor cargado solo si este se
encuentra entre los valores inicial o final, de lo contrario devuelve un
False. El programa debe cargar el valor devuelto por la función a una
lista de números solo si dicho valor es un valor entero (para saber qué
tipo de valor es, se puede utilizar la función isinstance(), la cual
necesita dos parámetros, el primero es el valor a controlar y el
segundo es el tipo de dato que deseamos controlar, por ejemplo:
isinstance(2, int) => True/ isinstance(“Hola”, float) => False /
isinstance(4, bool) => False / isinstance(True, bool) => True). Al final
de la carga, se deben mostrar todos los números cargados en la lista.
"""
from Modulos import verificar_numero


def test():
    inicio = int(input("Ingrese desde donde comienza el intervalo de control del número: "))
    fin = int(input("Ingrese hasta donde termina el intervalo de control del número: "))
    n = int(input("Ingrese la cantidad de números que quiere ingresar: "))
    lista_numeros = []
    for i in range(n):
        retorno = verificar_numero(inicio, fin)
        if retorno != False:
            lista_numeros.append(retorno)
    if len(lista_numeros) != 0:
        print("La lista quedo: ", lista_numeros)
    else:
        print("Todos los números cargados, no estuvierón dentro del intervalo!!")


if __name__ == '__main__':
    test()
