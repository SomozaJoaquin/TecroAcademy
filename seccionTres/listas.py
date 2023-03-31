mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista + mi_lista2
print(type(mi_lista))

otra_lista = ["hola", 55, 6.1]
print(type(otra_lista))

# Ver el largo de la lista
resultado = len(mi_lista)
print(resultado)

# Ver elemento con indice 0
resultado = otra_lista[0]
print(resultado)

# Concatenar listas
print(mi_lista3)

# Modificar una lista
mi_lista3[0] = "alfa"
print(mi_lista3)

# Agregar elemento a una lista
mi_lista3.append("g")
print(mi_lista3)

# Eliminar elemento de una lista
eliminado = mi_lista3.pop(0)
print(mi_lista3)
print(eliminado)

# Ordenar una lista alfabeticamente
# no devuelve nada, por ende no se puede guardar en una var
mi_lista4 = ["g", "o","b", "m","c"]
mi_lista4.sort()
print(mi_lista4)

# Invertir el orden de la lista
mi_lista4.reverse()
print(mi_lista4)