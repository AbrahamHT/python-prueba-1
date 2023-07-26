
def area_cilindro(r):
    A=3.14*r**2
    print(f"El area del cilindro es :{A}")
    return A

r=float(input("Ingrese radio de el Cilindro: "))

def volumen_cilindro(h):
    P=area_cilindro(r)
    V=P*h
    print(f"El columen del cilindro es:{V}")
h=float(input("Ingrese haltura de el Cilindro: "))
volumen_cilindro(h)
