import zipfile
import shutil
'''
Codigo para poder comprimir archivos
mi_zip = zipfile.ZipFile("archivo_comprimido.zip","w")
mi_zip.write("mi_texto_a.txt")
mi_zip.write("mi_texto_b.txt")
mi_zip.close()

'''

'''
Metodo para descomprimir archivos.
zip_abierto = zipfile.ZipFile("archivo_comprimido.zip","r")
zip_abierto.extractall()

'''

'''
Recorre las carpetas que le seleccionamos y comprime lo que encuentra.
carpeta_origen = "D:\\TecroAcademy\\python\\seccionNueve\\carpeta_prueba"
archivo_destino = "Todo_comprimido"
shutil.make_archive(archivo_destino,"zip",carpeta_origen)
'''
'''
Metodo para descomprimir todo lo que encutra en ciertas carpetas.
shutil.unpack_archive("Todo_comprimido.zip","Extraccion_terminada","zip")
'''


