import os

# Ver la ruta
'''ruta = os.getcwd()
print(ruta)'''

# Para cambiar la ruta de trabajo
'''ruta = os.chdir("D:\\TecroAcademy\\python\\seccionSeis\\nuevaRuta")
print(ruta)
archivo = open("otro_archivo.txt")
print(archivo.read())'''

#Asi, se podria crear una nueva carpeta desde aca.
# os.makedirs("D:\\TecroAcademy\\python\\seccionSeis\\nuevaCarpeta")

ruta = "D:\\TecroAcademy\\python\\seccionSeis\\prueba.txt"

elemento = os.path.basename(ruta)
print(elemento)
# Vemos hasta la carpeta anterior.
elemento2 = os.path.dirname(ruta)
print(elemento2)
# Muestra ambos pero los separa.
elemento3 = os.path.split(ruta)
print(elemento3)

# Eliminar carpeta
# os.rmdir("ACA VA LA RUTA")
