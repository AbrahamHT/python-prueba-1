def nivel_empleado(N):
    eur=2400 * N
    if N == 0.0:
        print(f"el nivel deel empleado es Inaceptable {N} su paga sera de {eur}")
    elif N == 0.4:
        print(f"el nivel deel empleado es Aceptabel {N} su paga sera de  {eur}")
    elif N >= 0.6:
        print(f"el nivel deel empleado es Meritorio {N} su paga sera de {eur}")

print("numeros aceptados son 0.0 , 0.4 , 0.6 o mayor \n")

N=float(input("Favor ingresar numero :"))
nivel_empleado(N)

