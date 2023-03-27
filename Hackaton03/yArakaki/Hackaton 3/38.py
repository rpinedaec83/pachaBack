def es_perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))
if es_perfecto(numero):
    print(numero, "es un número perfecto.")
else:
    print(numero, "no es un número perfecto.")
