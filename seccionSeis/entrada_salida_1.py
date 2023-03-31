# Abrir un archivo de la pc
mi_archivo = open("prueba.txt")
mi_archivo2 = open("prueba2.txt")

# Leer ese archivo
#print(mi_archivo.read())

# Leer de a una linea, al ser string tiene sus metodos.
una_linea = mi_archivo.readline()
print(una_linea.upper())

# Elimina el salto de linea.
una_linea = mi_archivo.readline()
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea)

# Se puede iterar dentro de las lineas.
for l in mi_archivo:
    print("Aqui dice: "+l)

#Otra opcion para imprimir todas las lineas en una lista seria
todas = mi_archivo2.readlines()

todas = todas.pop()
print(todas)








#Cerrar ese archivo.
mi_archivo.close()