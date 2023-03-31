precio_cafe = [("capuchino",1.5),("expresso",2),("Moka",1.9)]

'''for cafe,precio in precio_cafe:
    print(cafe)
    print(precio)
    print(precio*0.45)'''

def cafe_mas_caro(lista_precio):
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe, precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return(cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precio_cafe)
print(f"El cafe mas caro es {cafe} y su precio es ${precio}.")