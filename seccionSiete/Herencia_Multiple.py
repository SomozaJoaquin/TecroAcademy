class Padre():
    def hablar(self):
        print("Hola")

class Madre():
    def reir(self):
        print("Jaja")

    def hablar(self):
        print("Que tal?")

# El orden va a ser prioridad a la hora de heredar un metodo que se llame igual.
class Hijo(Madre,Padre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
mi_nieto.hablar()

# Asi vemos el orden de resolucion de la herencia de Nieto.
print(Nieto.__mro__)