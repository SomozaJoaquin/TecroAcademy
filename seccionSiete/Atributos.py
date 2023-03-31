# Atributos de instancia.

class Pajaro:
    # Atributos de clase.
    alas = True

    def __init__(self, color,especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro("negro", "Tucan")

palabra = "Hola"

print(mi_pajaro.color)
print(mi_pajaro.especie)
print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")
# Se puede llamar tanto desde la clase como del objeto.
print(Pajaro.alas)
print(mi_pajaro.alas)

