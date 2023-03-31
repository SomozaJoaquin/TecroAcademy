def suma(**kwargs):
    total = 0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total = total + valor
    return total

print(suma(x=3,y=5,z=2))
print("\n")


def suma2(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")


    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [200,100,2,3]
kwargs = {"x":"uno","y":"dos","z":"tres"}
suma2(15,59,*args,**kwargs)

