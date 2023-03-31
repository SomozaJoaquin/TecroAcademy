'''Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.'''

def devolver_distintos(int1,int2,int3):
    total = 0
    for numero in int1,int2,int3:
        total = total + numero

    if total > 15:
        print(max(int1,int2,int3))
    elif total < 10:
        print(min(int1,int2,int3))
    else:
        lista_ordenada = sorted([int1, int2, int3])
        print(lista_ordenada[1])


devolver_distintos(7,0,8)

