monedas = 5

while monedas > 0 and monedas != 1:
        print(f"Tengo {monedas} monedas")
        monedas = monedas -1
        if monedas == 1:
            print(f"Tengo {monedas} moneda")
            monedas = monedas - 1
else:
    print("No tengo mas dinero")

respuesta = "s"
while respuesta == "s":
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")

## pass sirve para guardar un lugar, se usa cuando no podes terminar el bucle ahora
## break corta un proceso.
## Continue saltea esa iteracion pero continua el blucle hasta su final
