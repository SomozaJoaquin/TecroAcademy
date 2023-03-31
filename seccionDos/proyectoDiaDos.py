nombre = input("Ingrese su nombre: ")
ventas = float(input("Ingrese sus ventas del mes: $"))
comision = round(ventas*13/100,2)
print(f"Ok {nombre} este mes ganaste ${comision}")

