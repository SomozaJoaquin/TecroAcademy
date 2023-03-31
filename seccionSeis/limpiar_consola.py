from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

# Importando y con este comando, limpiamos la consola.
system("cls")

print(f"Tu nombres es {nombre} y tienes {edad} años")
