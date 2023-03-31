class CD:
    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones


    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el cd")

mi_cd = CD("Pink Floyd", "The Wall", 24)
mi_cd2 = CD("Algo borrable","deleteable",0)
print(mi_cd)
print(len(mi_cd))


# Opcion para eliminar alguna instancia creada
del mi_cd2
