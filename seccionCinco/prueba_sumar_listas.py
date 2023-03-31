'''lista_numeros = [1,3,4,5,-1]
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return  False
        else:
            pass
    return True'''
'''
def chequear_lista(lista1):
    lista_3_cifras = []
    for numero in lista1:
        if numero in range(100,1000):
           lista_3_cifras.append(numero)
        else:
            pass
    return lista_3_cifras

resultado_lista = chequear_lista([828,99,600])
print(resultado_lista)'''

'''lista_numeros = [1, 50, 500, 5000, 750]  # 6301


def suma_menores(lista_numeros):
    '''
    #Suma un conjunto de valores en una lista
'''
    suma = 0

    for numero in lista_numeros:
        if numero in range(0, 1000):
            suma += numero
    return suma


print(suma_menores(lista_numeros))
'''

lista_numeros = [1, 50, 502, 755, 34]  # 50 + 502 + 34 = 586
def cantidad_pares(lista_numeros):
    suma_pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            suma_pares += numero
    return suma_pares

print(cantidad_pares(lista_numeros))