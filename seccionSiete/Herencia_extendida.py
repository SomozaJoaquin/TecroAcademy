class Animal():

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        # Con el metodo super. puedo traer cosas del elemento padre.
        super().__init__(edad,color)
        #self.edad = edad
        #self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio")

    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")



piolin = Pajaro(2,"Blanco",60)

# Metodo heredado sin modificacion, lo sobreescribe.
piolin.nacer()

# Metodo heredado modificado
piolin.hablar()

# Metodos completamente nuevos
piolin.volar(20)

mi_animal = Animal(5,"negro")
