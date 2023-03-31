# Analizador de texto
# 1 - Pedir al usuario que ingrese un texto *
# 2 - Tambien que ingrese 3 letras a eleccion *
# 3 - Hacer 5 tipo de analisis y devolver
#   a - Cuantas veces aparece cada letra que eligio. (Almacenar esas letras en una lista y usar algun metodo. buscarlas en minuscula. *
#   b - Cuantas palabras hay en total en el texto. *
#   c - Informar cual es la primer y la ultima letra. *
#   d - Mostrar el texto de manera inversa. *
#   e - Aparece la palabra Phyton en el texto? (Usar boolean + diccionario)

texto_pedido = input("Ingrese un texto: ")
texto_pedido = texto_pedido.lower()
letras = []

print("A continuacion debera ingresar 3 letras")
letras.append(input("Ingrese su primera letra: ").lower())
letras.append(input("Ingrese su segunda letra: ").lower())
letras.append(input("Ingrese su tercer letra: ").lower())
print("\n")

print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto_pedido.count(letras[0])
cantidad_letras2 = texto_pedido.count(letras[1])
cantidad_letras3 = texto_pedido.count(letras[2])

print(f"La letra '{letras[0]}' se repite {cantidad_letras1} veces")
print(f"La letra '{letras[1]}' se repite {cantidad_letras2} veces")
print(f"La letra '{letras[2]}' se repite {cantidad_letras3} veces")
print("\n")

print("CANTIDAD DE PALABRAS")
cantidad_palabras = len(texto_pedido.split(" "))
print(f"Este es un texto de {cantidad_palabras} palabras")
print("\n")

print("PRIMER Y ULTIMA LETRA")
texto_unido = list(texto_pedido)
primer_letra = texto_unido[0]
ultima_letra = texto_unido[-1]
print(f"La primer letra de su texto es la '{primer_letra}' y la ultima es la '{ultima_letra}'")
print("\n")

print("TEXTO INVERTIDO")
texto_unido.reverse()
print(f"Su texto de manera invertida quedaria asi {texto_unido}")
print("\n")

print("¿APARECE LA PALABRA PYTHON?")
buscar_python = "python" in texto_pedido
dic = {True:"si",False:"no"}
print(f"La palabra 'Python', {dic[buscar_python]} se encuentra en el texto")



