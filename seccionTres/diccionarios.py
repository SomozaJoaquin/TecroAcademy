diccionario = {"c1":"valor1","c2":"valor2"}

print(type(diccionario))
print(diccionario)

# Busquedas
resultado = diccionario["c2"]
print(resultado)

# Todo tipo de datos
cliente = {"nombre":"Juan","apellido":"Fuentes","peso":88,"talla":1.80}
consulta = (cliente["peso"])
print(consulta)

# Diccionarios dentro de diccionarios
dic = {"c1":44, "c2":[10,20,30],"c3": {"s1":100,"s2":200}}
print(dic["c2"][1])
print(dic["c3"]["s2"])

# Ejercicio
dic2 = {"c1":["a","b","c"],"c2":["d","e","f"]}
print(dic2["c2"][1].upper())

# Agregar un elemento o sobreescribirlo
dic3 = {1:"a",2:"b"}
print(dic3)
dic3[3] = "c"
dic3[2] = "s"
print(dic3)
# Para ver que tiene un dic.
print(dic3.keys())
print(dic3.values())
print(dic3.items())


