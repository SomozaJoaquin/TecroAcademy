from pathlib import Path,PureWindowsPath

#poniendo esta ruta podes abirlo desde cualquier sistema operativo.
carpeta = Path("D:/TecroAcademy/python/seccionSeis/nuevaRuta")
archivo = carpeta / "otro_archivo.txt"

'''mi_archivo = open(archivo)
print(mi_archivo.read())'''

# Sirve para leer un archivo sin tener que poner open
print(archivo.read_text())

# Extrae el nombre mediante el objeto path.
print(archivo.name)

# Suffix, devuelve el tipo de archivo
print(archivo.suffix)

# Ver si existe un archivo, en este caso el almacenado en la var carpeta.
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")

# Sirve para crear una ruta de window
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)