class Pajaro:
    # Atributos de clase.
    alas = True

    def __init__(self, color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")

    # Metodos de clase:
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    # Metodo estatico
    @staticmethod
    def mirar():
        print("El pajaro mira.")


Pajaro.poner_huevos(3)
Pajaro.mirar()
piolin = Pajaro("amarillo","Canario")

''' 
Los metodos de instancia pueden:
    - Acceder y modificar un atributo del objeto
    - Acceder a otros metodos
    - Modificar el estado de la clase
'''

piolin.pintar_negro()
piolin.volar(20)
piolin.alas = False
print(piolin.alas)

'''
Metodos de clase:
    - Se definen con un @classmethod
    - Pueden acceder a los atributos de clase
    - No necesitan una instancia para poder ejecutarse.
    - No pueden acceder a los atributos dentro de una instancia.
    
'''

'''
Metodos estaticos:
    - NO pueden modificar el estado de una instancia
    - No pueden cambiar el atributo de la clase.
    - Sirve para asegurar objetos que no quieres que modifiquen instancias.
'''