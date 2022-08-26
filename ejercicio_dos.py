"""
2. Cree un programa con las siguientes funciones:
a. Una función que genere una lista con 5 elementos enteros
aleatorios que sean números entre 1 y 3
b. Una función que controle si el primer elemento de la lista es un
1, en caso de que haya un 2 o 3 mezclar la lista y volver a
controlar hasta que haya un 1.
c. Muestre la lista
"""
from Modulos import cargarLista, verificarLista


def test():
    listaNumeros = cargarLista()
    flag = False
    while (flag == False):
        flag = verificarLista(listaNumeros, flag)
    print("La lista quedo: ", listaNumeros)


if __name__ == "__main__":
    test()
