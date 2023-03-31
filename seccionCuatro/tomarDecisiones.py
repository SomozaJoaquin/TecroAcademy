x = 10 > 9

if x:
    print("Es correcto")
else:
    print("Es incorrecto")

mascota = "perro"

if mascota == "gato":
    print("tienes un gato")
elif mascota=="perro" :
    print("tienes un perro")
else:
    print("No se que animal tienes")
print("\n")

edad = 17
calificacion = 2
if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Has aprobado")
    else:
        print("Has desaprobado")
else :
    print("Eres un adulto")