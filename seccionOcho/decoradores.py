'''
En python es un objeto. incluso las funciones, entonces se puede asignar una funciona  una variable.
Tambien puedes pasar una funcion como argumento de una funcion.
Tambien podemos definir una funcion dentro de una funcion.

'''
def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

#mi_funcion = mayuscula
#mi_funcion("python")

def una_funcion(funcion):
    return funcion

#una_funcion(mayuscula("probando"))

operacion = cambiar_letras("may")
operacion("palabra")