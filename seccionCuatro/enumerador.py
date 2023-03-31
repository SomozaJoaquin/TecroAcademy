lista = ["a","b","c","d"]
indice = 0

for indice,item in enumerate(lista):
    print(indice,item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)
print([1][0])

palabra = "Python"

lista_indices = list(enumerate(palabra))
print(lista_indices)