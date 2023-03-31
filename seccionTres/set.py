mi_set = set([1,2,3,4,("a","b","c"),5,1,2,3,4])
print(type(mi_set))
print(mi_set)

# No tienen indice.
# No muestra repeticiones.
# No acepta listas ni dic dentro.
# Si acepta tuples

otro_set = {10,20,30}
print(len(otro_set))
print(2 in otro_set)

# Se pueden unir pero sigue sin repetir
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

# Agregar
s1.add(14)
print(s1)
# Borrar
s1.remove(2)
print(s1)
# Descargar con discart
# Eliminar aleatoriamente .pop
# Vaciar el set con .clear
