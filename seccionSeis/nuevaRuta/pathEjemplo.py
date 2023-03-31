from pathlib import Path

guia = Path(Path.home(),"Europa")
guia2 = Path(Path.home(),"Europa")

# Un bucle que muestre cada .txt que encuentre en todas las carpetas del path home Europa
for txt in Path(guia).glob("**/*.txt"):
    print(txt)
print("\n")
guia2 = Path("Europa","España","Barcelona","SagradaFamilia.txt")
en_europa = guia2.relative_to(Path("Europa"))
en_espania = guia2.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espania)