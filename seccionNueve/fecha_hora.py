from datetime import *

mi_hora = datetime(1994,11,23,14,24)
print(mi_hora.minute)

mi_dia = date.today()
print(mi_dia)

# Como modificar algun dato.
mi_hora = mi_hora.replace(year = 2023)

nacimiento = date(1995,3,5)
defuncion = date(2095,6,19)

vida = defuncion - nacimiento
print(vida)

despierto = datetime(2023,4,3,7,45)
duermo = datetime(2023,4,3,23,59)

vigilia = duermo - despierto
print(vigilia)


minutos = datetime.now().minute
print(minutos)