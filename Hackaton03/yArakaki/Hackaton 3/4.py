a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a <= b and a <= c:
    menor = a
    if b <= c:
        medio = b
        mayor = c
    else:
        medio = c
        mayor = b
elif b <= a and b <= c:
    menor = b
    if a <= c:
        medio = a
        mayor = c
    else:
        medio = c
        mayor = a
else:
    menor = c
    if a <= b:
        medio = a
        mayor = b
    else:
        medio = b
        mayor = a

print("Los números ordenados de menor a mayor son:", menor, medio, mayor)
