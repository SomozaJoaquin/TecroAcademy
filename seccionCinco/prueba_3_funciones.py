from random import randint
'''Crea una función (llamada lanzar_moneda) que devuelva el resultado
de lanzar una moneda (al azar).'''

def lanzar_moneda():
    moneda = randint(1,2)
    if moneda == 1:
        print("Cara")
        return "Cara"

    else:
        print("Cruz")
        return "Cruz"



'''Crea una segunda función (llamada probar_suerte), 
que tome dos argumentos: el primero, debe ser el resultado del
 lanzamiento de la moneda. El segundo argumento, será una lista
  de números cualquiera (debes crear una lista con valores y llamarla
   lista_numeros).'''
'''
Si se le proporciona una "Cara", debe mostrar el mensaje al usuario:
 "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
Si se le proporciona una "Cruz", debe imprimir en pantalla:
 "La lista fue salvada" y devolver la lista intacta.'''
lista_numeros = [1,2,3,4,5,6]
def probar_suerte(lanzar_moneda,lista_numeros):
    if lanzar_moneda == "Cara":
        lista_numeros.clear()
        return lista_numeros, "La lista se autodestruyo"
    else:
        return lista_numeros, "La lista fue salvada"
suerte = lanzar_moneda()
print(probar_suerte(suerte,lista_numeros))

## OTRA SOLUCION
from random import *

def lanzar_moneda():
    moneda = choice(["Cara", "Cruz"])
    return moneda

lista_numeros = [1, 2, 3, 4, 5, 6]

def probar_suerte(moneda, lista_numeros):
    if moneda == "Cara":
        lista_numeros.clear()
        print("La lista se autodestruyo")
    else:
        print("La lista fue salvada")
    return lista_numeros
