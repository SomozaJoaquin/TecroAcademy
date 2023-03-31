menor = min(58,96,72,64,35)
print(menor)
mayor = max(58,96,72,64,35)
print(mayor)

lista = [58,96,72,64,35]
print(max(lista))
print(f"El menor es {menor} y el mayor es {mayor}")

lista_nombre = ["Juan","Pablo","Alicia", "Carlos"]
print(min(lista_nombre))
print(max(lista_nombre))

# Primero busca entre las mayusculas
cadena_str = "carlos"
print(min(cadena_str))

# Si no le pongo el .values me traeria el menor indice.
dic = {"C1":45,"C2":11}
print(min(dic.values()))