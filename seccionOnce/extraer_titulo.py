import bs4
import requests

url_base = "http://books.toscrape.com/catalogue/page-{}.html"

'''for n in range(1,11):
    print(url_base.format(n))'''

resultado = requests.get(url_base.format("1"))
sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

libros = sopa.select(".product_pod")

# Trae el libro con indice 0 que tiene las clases star-rating y Three, esto del elemento padre con clase .product_pod
'''ejemplo = libros[0].select(".star-rating.Four")
print(ejemplo)'''

# Trae los elementos "a" que tenga ese libro en indice 0, y de ambas en este caso, muestra el title.
ejemplo = libros[0].select("a")[1]["title"]
print(ejemplo)







