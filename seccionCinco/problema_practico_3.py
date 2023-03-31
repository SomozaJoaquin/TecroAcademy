'''Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False'''


def devolucion(*args):
    contador_ceros = 0
    consecutivos = False

    for arg in args:
        if arg == 0:
            contador_ceros += 1
            if contador_ceros == 2:
                consecutivos = True
        else:
            contador_ceros = 0
    return consecutivos
print(devolucion(1,2,3,0,4,5,0))