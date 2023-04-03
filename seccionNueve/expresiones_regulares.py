import re

texto = "Si necesitas ayuda llama al (658)-589-9977 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in texto
print(palabra)

patron = "ayuda"
# Buscamos si aparece x ayuda en x texto.
#busqueda = re.search(patron, texto)
#print(busqueda)

# Buscamos mas de una aparicion y la cantidad de veces que aparece.
busqueda = re.findall(patron, texto)
print(len(busqueda))

hallazgo = re.findall(patron, texto)
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

texto2 = "Llama al 445-442-4232 ya mismo"
patron2 = r"\d\d\d-\d\d\d-\d\d\d\d"
# otra forma seria
patron2 = r"\d{3}-\d{3}-\d{4}"

# Podemos encontrar el resultado especifico con esas condiciones.
resultado2 = re.search(patron2,texto2)
print(resultado2.group())

clave = input("Clave : ")
patron3 = r"\D{1}\w{7}"

chequear = re.search(patron3, clave)
print(f"Patron3 {chequear}")



texto3 = "No atendemos los lunes por la tarde"
buscar = re.search(r"lunes|martes", texto3)
print(buscar)

# Separar la frase por medio de comillas, anulando los espacios vacios.
buscar = re.findall(r'[^\s]+', texto3)
print(buscar)
# Y lo vuelva a unir
print("".join(buscar))