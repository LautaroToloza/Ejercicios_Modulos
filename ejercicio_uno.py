"""
1. Cree un programa que genere un numero aleatorio entre 1 y 100 (no
se debe mostrar el numero en pantalla). El usuario debe tratar de
adivinar el numero ingresado. Cada vez que se ingrese un numero se
debe mostrar un mensaje “Gano” si es igual al generado o “El
numero aleatorio es mayor” o “El numero aleatorio es menor”.
Mostrar cuantos intentos necesito el usuario para ganar.
"""

from Modulos import crearNumeroAleatorio, mostrarMensajeNumerosAleatorio


def test():
    num = crearNumeroAleatorio()
    flag = False
    while (flag == False):
        op = int(input("Ingrese el número que creé que salio como aleatorio: "))
        flag = mostrarMensajeNumerosAleatorio(num, op, flag)


if __name__ == "__main__":
    test()
