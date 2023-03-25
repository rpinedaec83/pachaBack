def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = mcd(num1, num2)

print("El M.C.D de", num1, "y", num2, "es:", resultado)