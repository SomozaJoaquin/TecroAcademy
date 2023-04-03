from collections import Counter, defaultdict, namedtuple

numeros = [6,7,2,2,2,4,5,6,6,6,2]
frase = "Al pan pan , al vino vino"
# Contador, tando de listas como de letras o cade de string.
print(Counter(numeros))
print(Counter("mississippi"))
print(Counter(frase.split()))

# Se puede aplicar directamente con metodos. O se le puede pasar por parametro al metodo.
serie = Counter([1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3])
print(serie.most_common())

# O imprimir directamente dentro de una lista.
print(list(serie))

# Default dict.
mi_dic = {"uno": "verde","dos": "azul","tres": "rojo"}
print(mi_dic["dos"])

# Deja un valor por defecto en caso de no encontrar.
mi_dic2 = defaultdict(lambda :"nada")
mi_dic2["uno"] = "verde"
print(mi_dic2["dos"])

mi_tupla = (500,18,65)
print(mi_tupla[1])
Persona = namedtuple("Persona", ["nombre","altura","peso"])
ariel = Persona("Ariel",1.70,60)

print(ariel.altura)