palabra = "python"

#Una forma de hacerlo.
#lista = []

#for letra in palabra:
#    lista.append(letra)
#print(lista)

# Otra forma de recorrer una palabra e ir agregando a una lista.
lista = [letra for letra in palabra]
print(lista)

# Crea una lista con los numeros dividido por dos, pares del 0 al 20
lista2 = [n/2 for n in range(0,21,2)]
print(lista2)

pies = [10,20,30,40,50]
metros = []
metros = [pie*3.281 for pie in pies]
print(metros)
