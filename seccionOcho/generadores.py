def min_funcion():
    return 4

def mi_generador():
    yield 4

print(min_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))

def generador2():
    for x in range(1,5):
        yield (x*10)

gen = generador2()
print(next(gen))
print(next(gen))
print(next(gen))

def mi_generador3():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g3 = mi_generador3()
print(next(g3))
print(next(g3))
print(next(g3))