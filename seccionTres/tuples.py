mi_tuple = (1,2,(1,20),4)

print(type(mi_tuple))
# Se lo puede consultar
print(mi_tuple[1])
print(mi_tuple[2][1])

# No se puede modificar pero si transformar
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

# Asignar el contenido a dif var
# siempre que sean la misma cantidad.
t = (1,2,3)
x,y,z = t
print(x,y,z)

u = (1,2,3,1,18)
print(len(u))
# Consultar cant de veces repetido un valor
print(u.count(1))
# Consultar numero de indice
print(u.index(3))
print(u[4])

