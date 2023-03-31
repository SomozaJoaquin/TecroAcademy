from statistics import mean

'''Crea una función  reducir_lista()
que tome una lista como argumento
y devuelva la misma lista, eliminando duplicados y
eliminando el valor más alto.
'''
lista_numeros = [1,2,15,7,2]
lista_numeros2 = []
lista_numeros2 = lista_numeros[0:1]
def reducir_lista(lista_numeros):
    for i in range(len(lista_numeros)):
        if lista_numeros[i] not in lista_numeros2:
            lista_numeros2.append(lista_numeros[i])

    lista_numeros2.sort()
    lista_numeros2.pop()
    return lista_numeros2

print(lista_numeros)
print(reducir_lista(lista_numeros))

'''
Crea una función promedio() que pueda recibir
 como argumento la lista devuelta por la anterior función,
  y que calcule el promedio de los valores de la misma.
   Debe devolver el resultado, sin imprimirlo.
'''
def promedio(lista_numeros2):
    promedio_calculado = mean(lista_numeros2)
    return promedio_calculado

print(promedio(lista_numeros2))