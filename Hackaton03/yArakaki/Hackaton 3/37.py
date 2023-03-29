def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultado = mcd(a, b)
print("El M.C.D de", a, "y", b, "es:", resultado)
