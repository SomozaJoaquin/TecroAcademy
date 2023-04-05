import bs4
import requests

# Crear url sin numero de pagina
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

# Lista vacia a los que se van a agregar los titulos con 4 o 5 estrellas.
titulos_rating_alto = []

# Iterar paginas
for pagina in range(1,3):
    # Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,"html.parser")

    # Seleccionar datos de los libros
    libros = sopa.select(".product_pod")
    for libro in libros:
        # Chequear que tengan 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            # Guadar titulo en variable
            titulo_libro = libro.select("a")[1]["title"]
            # Agregar libro a la lista.
            titulos_rating_alto.append(titulo_libro)

# Solo se imprimen los de las paginas 1 y 2 porque tardaba mucho en devolver una respuestas si se ponia a analizar de la 1 a la 50.
# Ver libros de 4 o 5 lineas en consola.
for t in titulos_rating_alto:
    print(t)