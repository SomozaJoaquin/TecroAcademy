'''
Herencia, es cuando una clase "hija" puede obtener metodos, atributos de una clase "padre"
osea que esta por sobre ella. Esto evita reescribir codigo y volver a definir metodos de nuevo.
DRY = dont repeat yourself
'''

class Animal():

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass


class Perro(Animal):
    pass

piolin = Pajaro(2,"Blanco")
piolin.nacer()
rope = Perro(4,"Marron")
rope.nacer()
print(rope.color)

# Ver de que clase hereda.
print(Pajaro.__bases__)

# Ver si tiene subclases
print(Animal.__subclasses__())