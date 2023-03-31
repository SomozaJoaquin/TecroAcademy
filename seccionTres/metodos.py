texto = "Este es el texto de Federico"
resultado = texto

print(resultado)

# Metodo upper
resultado1 = texto.upper()
print(resultado1)

# Metodo minuscula
resultado2 = texto.lower()
print(resultado2)

# Metodo para separar por espacios o letras
resultado3 = texto.split()
#resultado3 = texto.split("t")
print(resultado3)

# Metodo para unir
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
# en la variable e unimos con lo que queramos la lista.
e = " ".join([a,b,c,d])
print(e)

# Metodo find cuando no encuentra arroja -1
resultado4 = texto.find("s")
print(resultado4)

# Metodo replace
resultado5 = texto.replace("Federico", "Joaquin")
print(resultado5)

