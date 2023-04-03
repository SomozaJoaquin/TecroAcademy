# Importar desde el paquete que queramos la funcion que queramos o por completo (*)
# Llamar al archivo y luego a la funcion deseada.
from Paquete_Joa import suma_y_resta
from Paquete_Joa.Subpaquete import saludo


suma_y_resta.suma(4,4)
suma_y_resta.resta(10,5)

saludo.hola()