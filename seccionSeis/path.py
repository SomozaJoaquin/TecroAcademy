from pathlib import Path

# Home devuelve una ruta absoluta al directorio del usuario actual
base = Path.home()
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
#print(base)
print(guia)
print(guia2)

# Parent devuelve el archivo anterior al ultimo.
print(guia.parent)