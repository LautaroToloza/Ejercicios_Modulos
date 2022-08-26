"""
6. Cree un programa que pregunta cuando usuarios se quieren cargar
en una lista. Se tiene que utilizar un módulo para la validación de
nombres y contraseñas de usuarios. Las funciones que debería
cumplir el módulo son las siguientes:

a. El nombre del usuario debe tener un mínimo de 6 caracteres y
un máximo de 12. Si el nombre ingresado tiene menos de 6
caracteres o más de 12, el programa debería avisar de la
situación y obligar a que el usuario ingrese un nombre válido.

b. Los usuarios solo pueden contar con valores alfanuméricos,
por lo que, si el nombre ingresado por el usuario, si no cumple
con dicha condición se debería avisar del error y pedirle al
usuario que ingrese un nuevo nombre (puede utilizar la
función isalnum(), la cual devuelve un True si el String cuenta
solo con valores alfanuméricos o un False en caso contrario).
El programa debe obligar a que el usuario ingrese un nombre
válido.

c. Si el nombre cumple con las condiciones anteriores, una
función debería enviar un True que le avise al resto del
programa que el nombre es apto para cargar.

d. Con respecto a la contraseña, debe tener un mínimo de 8
caracteres, si la cantidad es menor el programa debe avisar del
error y obligar al usuario a ingresar una contraseña válida.

e. La contraseña debe tener si o si: letras mayúsculas,
minúsculas, números, al menos un carácter no alfanumérico y
no debe tener espacios en blanco. Como recomendación,
puede utilizar las funciones islower() (la función devuelve un
True solo si las letras que se encuentran en la cadena son todas
minúsculas), issupper() (devuelve un True si la cadena que
tiene que controlar todas las letras que contenga están en
mayúsculas).

f. Si la contraseña cumple con las condiciones anteriores, se
debería enviar un True avisando que la contraseña está en
condición de cargar.

g. Solo si la contraseña y el nombre de usuario están en
condiciones de cargar, se debería cargar los datos a la lista
general. La forma de cargar es la siguiente: cree una lista que
guarde el nombre y la contraseña y guarde dicha lista en la
lista general. Una vez cargados los nombres, muestre en
forma de lista los datos cargados en la lista general.
"""
from Modulos import verificar_nombre_usuario, verificar_clave


def test():
    usuario = verificar_nombre_usuario()
    clave = verificar_clave()
    print("\nFinalizó el programa!!")


if __name__ == "__main__":
    test()
