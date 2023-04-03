import os
import shutil
import send2trash
# Podemos ver donde estamos parados
print(os.getcwd())

# Crear y abrir un archivo editabble
archivo = open("curso.txt", "w")
archivo.write("Texto de prueba")

print(os.listdir())



# Cerrar archivo.
archivo.close()

'''Como mover archivos.
        Importamos shutil
        ponemos .move nombre del archivo y nueva ruta de destino
        en este caso ira al dia anterior.
'''
# Solo se puede ejecutar una vez ya que despues tira error porque encuentra un archivo con ese nombre.
#shutil.move("curso.txt", "D:\\TecroAcademy\\python\\seccionCuatro")

# Remueve directamente el archivo
#os.unlink()

# Sirve para eliminar pero que vaya a papelera de reciclaje.
#send2trash.send2trash()

# Recorre carpetas y muestra lo que encuentra.
print(os.walk("D:\\TecroAcademy\\python\\seccionDos"))
ruta = "D:\\TecroAcademy\\python\\seccionNueve"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
       print(f"\t{sub}")
    print("Los archivos son: ")
    for arch in archivo:
        if arch.startswith("2015"):
            print(f"\t{arch}")
    print("\n")