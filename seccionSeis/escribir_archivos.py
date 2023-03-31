#Abrir un texto, arranca de 0 y se puede escribir.
# Si al final usamos "a" podemos hacer lo mismo solo que agrega al final sin borrar lo que ya habia.
# Con "w" se escribe pero elimina lo que tenia de antemano.
archivo = open("prueba.txt","a")
archivo.write("Soy el nuevo texto\n")
archivo.write("se peude escribir en distintas lineas usando '\\n' \n")
archivo.write('''O utilizando 3 comillas
y saltos de linea en el editor
''')

#casi no se usa
archivo.writelines(["hola", "mundo", "aqui","estoy"])

# se le puede pasar una lista.
lista = ["hola", "mundo", "aqui","estoy"]
for l in lista:
    archivo.writelines(l + "\n")















archivo.close()