mi_archivo = open("mi_archivo.txt")
mi_archivo.close()

nueva_apertura = open("mi_archivo.txt","w")
nueva_apertura.write("Nuevo texto")

nueva_apertura.close()



'''
archivo = open("mi_archivo.txt")
archivo.close()

nuevo = open("mi_archivo.txt","w")
nuevo.write("Nuevo texto")

nuevo.close()

nuevo = open("mi_archivo.txt","r")
print(nuevo.read())

'''