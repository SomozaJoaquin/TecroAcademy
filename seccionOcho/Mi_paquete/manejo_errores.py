def suma():
        n1 = int(input("Numero 1: "))
        n2 = int(input("Numero 2: "))
        print(n1 + n2)
        print("Gracias por sumar")




#codigo a probar
try:
    suma()
# Codigo a ejecutar si hay un error
except:
    print("Algo no ha salido bien.")
# Codigo a ejecutar si no hay un error
else:
    print("Hiciste todo bien")
# Codigo que se va a ejecutar de todos modos
finally:
    print("Eso fue todo.")
