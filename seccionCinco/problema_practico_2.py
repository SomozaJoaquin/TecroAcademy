'''Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']'''

def devolver_letras(palabra):
    mi_set = set(palabra)

    for letra in palabra:
        mi_set.add(letra)

    palabra_lista = sorted(list(mi_set))
    return palabra_lista
print(devolver_letras("entretenido"))
