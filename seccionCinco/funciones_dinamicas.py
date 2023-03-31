def chequear_3_cifras(numero):
    return numero in range(100,1000)

suma = 444 + 234
resultado = chequear_3_cifras(suma)
print(resultado)

def chequear_lista(lista1):
    lista_3_cifras = []
    for numero in lista1:
        if numero in range(100,1000):
           lista_3_cifras.append(numero)
        else:
            pass
    return lista_3_cifras

resultado_lista = chequear_lista([828,99,600])
print(resultado_lista)


