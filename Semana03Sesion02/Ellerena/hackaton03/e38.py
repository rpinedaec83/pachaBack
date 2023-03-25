def es_perfecto(num):
    div = 1
    suma = 0
    while div < num:
        if num % div == 0:
            suma += div
            div += 1
    if suma == num:
        return True
    else:
        return False

num = int(input("Ingrese un número: "))

if es_perfecto(num):
    print(num, "es un número perfecto.")
else:
    print(num, "no es un número perfecto.")