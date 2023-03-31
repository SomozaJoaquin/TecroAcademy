def suma(*args):
    total = 0
    for arg in args:
        total = total+arg
    return total

print(suma(6,7,5,1))

# Otra manera mas sencilla
def sumar2(*args):
    return sum(args)

print(suma(2,1,3,3))