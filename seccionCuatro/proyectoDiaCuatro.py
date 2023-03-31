from random import *

# Adivinar el numero!
'''
# preguntar un nombre y dar consigna de que debe adivinar un numero del 1 al 100 en 8
intentos.
# En cada intento el programa puede responder 4 cosas distintas:
  1. numero > 1 o < 100 NO ESTA PERMITIDO
  2. numero menor, dira que es incorrecto y que el programa eligio un numero mayor
  3. numero mayor, dira que es incorrecto y que el programa eligio un numero menor
  4. Numero correcto. Y cantidad de intentos utilizados.
'''
nombre = input("Bienvenido, por favor ingresa tu nombre y presiona la tecla 'Enter': ")
print(f"Hola {nombre}, estoy pensando un numero del 1 al 100, tienes 8 intentos para adivinarlo. ¡Intentalo!")

numero_elegido =  int(input("Ingrese que crea que estoy pensando: "))

numero_random = randint(1,100)

print(numero_random)

intentos = 0

while intentos < 8:
    if (numero_elegido  < -1) or (numero_elegido > 100) :
        print("Recuerda seleccionar un numero del 1 al 100")
        intentos += 1
        print(f"Vas por el intento {intentos} de 8 intentos.")
        numero_elegido = int(input("ingresa nuevamente otro numero: "))
    elif (numero_elegido < numero_random) :
        print("El numero que pensé es mayor al que acabas de escribir.")
        intentos += 1
        print(f"Vas por el intento {intentos} de 8 intentos.")
        numero_elegido = int(input("ingresa nuevamente otro numero: "))
    elif (numero_elegido > numero_random) :
        print("El numero que pensé es menor al que acabas de escribir.")
        intentos += 1
        print(f"Vas por el intento {intentos} de 8 intentos.")
        numero_elegido = int(input("ingresa nuevamente otro numero: "))
    else :
        print(f"¡Adivinaste! Utilizaste {intentos} intentos.")
        break
if intentos == 8:
    print("Te quedaste sin intentos, vuelve a intentarlo.")

