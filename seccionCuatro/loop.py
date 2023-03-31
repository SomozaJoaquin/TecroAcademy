lista = ["a", "b", "c", "d"]

for letra in lista:
    numero_letra = lista.index(letra) +1
    #print("Letra " + letra)
    print(f"Letra {numero_letra}: {letra}")

lista2 = ["pablo","laura","fede","luis","julia"]
for nombre in lista2:
    if nombre.startswith("l"):
        print(f"{nombre} es un nombre que comienza con la letra L")
    else:
        print(f"{nombre} es un nombre que NO comienza con la letra L")

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
print(mi_valor)

palabra= "python"

for letra in palabra:
    print(letra)
print("\n")
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print("\n")

dic = {"valor1":"a","valor2":"b","valor3":"c"}

for a,b in dic.items():
    print(a,b)
