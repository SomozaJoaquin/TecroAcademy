# Se importa todo de libreria random.
from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio1 = round(uniform(1,5),1)
print(aleatorio1)

# Devuelve un numero entre 0 y 1
aleatorio2 = random()
print(aleatorio2)

colores = ["azul","rojo","verde","amarillo"]
aleatorio3 = choice(colores)
print(aleatorio3)

# Shuffle sirve para mezclar!
numeros = list(range(5,51,5))
shuffle(numeros)
print(numeros)