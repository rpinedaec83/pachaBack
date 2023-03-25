a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

if a >= b and a >= c:
    print("El número mayor es:", a)
elif b >= a and b >= c:
    print("El número mayor es:", b)
else:
    print("El número mayor es:", c)
