import bs4
import requests
resultado = requests.get("https://escueladirecta-blog.blogspot.com/2023/03/redescubre-el-poder-de-excel-con-power.html")

sopa = bs4.BeautifulSoup(resultado.text,"html.parser")
# Mediante el select puedo obtener el contenido de la etiqueta que quiero en una lista.
print(sopa.select("title"))
print(len(sopa.select("p")))
print(sopa.select("h1"))
#Al ser una lista puedo obtener un indice en particular.
print(sopa.select("title")[0].get_text())

#Por cada p que encuentra, lo imprime pero unicamente el texto que tiene dentro.
parrafo_especial = sopa.select("p")
for p in parrafo_especial:
    print(p.getText())

# Obtengo los elementos que tienen la clase title
# sopa.select(".clase etiqueta")
# sopa.select(".clase etiqueta")
columna_lateral = sopa.select(".title")
print(columna_lateral)

# Extraccion de imagenes.
url2 = requests.get("https://www.escueladirecta.com/courses")
sopa2 = bs4.BeautifulSoup(url2.text,"html.parser")

imagenes = sopa2.select(".course-box-image")[0]["src"]
print(imagenes)
'''for imagen in imagenes:
    print(imagen)'''

# Al obtener la imagen a descargar, al venir en binario, la vamos a abrir, escribir binario.
#
primer_imagen = requests.get(imagenes)
f = open("mi_imagen.jpg", "wb")
f.write(primer_imagen.content)
f.close()