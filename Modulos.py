import random, math


def crearNumeroAleatorio():
    num = random.randint(1, 100)
    return num


def mostrarMensajeNumerosAleatorio(num, op, flag):
    if num == op:
        print("Ganó!!")
        flag = True
    elif num < op:
        print("El número aleatorio es menor!!")
    else:
        print("El número aleatorio es mayor!!")
    return flag


def cargarLista():
    lista = []
    for i in range(5):
        lista.append(random.randint(1, 3))
    return lista


def verificarLista(lista, flag):
    if lista[0] != 1:
        random.shuffle(lista)
    else:
        flag = True
    return flag


def calcular_factorial(num):
    fac = math.factorial(num)
    return fac


def mayor_numero(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        may = n1
    elif n2 > n3:
        may = n2
    else:
        may = n3
    return may


def menor_numero(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        men = n1
    elif n2 < n3:
        men = n2
    else:
        men = n3
    return men


def verificar_nombre_usuario():
    flag = False
    usuario = input("Ingrese su usuario: ")
    while (not flag):
        if len(usuario) < 6 or len(usuario) > 12:
            print("Error, el usuario tiene que tener como mínimo 6 caracteres y máximo 12!!")
        if usuario.isalnum() == False:
            print("Error, el usuario solo tiene que tener caracteres alfanuméricos!!")
        else:
            print("El nombre es apto para usar!!")
            flag = True
        if not flag:
            usuario = input("Ingrese nuevamente su usuario: ")
    return usuario


def verificar_clave():
    flag = False
    letras = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    mayusculas = letras.upper()
    numeros = "0123456789"
    clave = input("Ingrese su contraseña: ")
    tiene_minuscula, tiene_mayuscula, tiene_numero, tiene_no_alfanumerico = False, False, False, False
    tiene_espacio = False
    while (not flag):
        if len(clave) < 8:
            print("Error, la contraseña tiene que tener mínimo 8 caracteres!!")
        for car in clave:
            if car == " ":
                print("Error, la contraseña no tiene que tener ningun espacio!!")
                tiene_espacio = True
                break
            else:
                if car in letras:
                    tiene_minuscula = True
                elif car in mayusculas:
                    tiene_mayuscula = True
                elif car in numeros:
                    tiene_numero = True
                else:
                    tiene_no_alfanumerico = True

        if not tiene_espacio:
            if tiene_minuscula and tiene_mayuscula and tiene_numero and tiene_no_alfanumerico:
                flag = True
        if flag:
            print("La contraseña cumple los requisitos!!")
        else:
            print("La contraseña no cumple los requisitos, intente nuevamente!!")
            clave = input("Ingrese su contraseña: ")
    return clave


def verificar_numero(inicio, fin):
    num = int(input("Ingrese un número: "))
    if num >= inicio and num <= fin:
        return num
    return False
