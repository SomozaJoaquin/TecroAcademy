nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,42,33]
ciudades = ["Lima","Madrid","Bs As"]

# Zip sirve para combinar listas
combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años, y vive en {ciudad}")