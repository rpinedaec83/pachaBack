def ejercicio01():
    numero = int(input('ingrese un numero para determinar la cantidad de dígitos: '))
    cant_digitos = len(str(numero))
    print(f'el número {numero} tiene {cant_digitos} dígitos')
def ejercicio02():
    numero = int(input('ingrese un numero para determinar si es negativo: '))
    if numero > 0:
        print(f'el número {numero} es positivo')
    else:
        print(f'el número {numero} es negativo')
def ejercicio03():
    numero = int(input("Ingrese un número: "))
    if numero % 10 == 4:
        print("El número termina en 4.")
    else:
        print("El número no termina en 4.")

def ejercicio04():
    print('ingrese 3 numeros: ')
    n1 = int(input('número 1: '))
    n2 = int(input('número 2: '))
    n3 = int(input('número 3: '))
    numeros = [n1,n2,n3]
    numeros.sort()
    print('los números ordenados de menor a mayor son :')
    for num in numeros:
        print(num)
def ejercicio05():
    zapatos = int(input("Ingrese el número de zapatos a comprar: "))
    precio_sin_descuento = zapatos * 80
    if zapatos > 10 & zapatos <=20:
        descuento = 0.1
    elif zapatos > 20 & zapatos<30:
        descuento = 0.2
    if zapatos > 30:
        descuento = 0.4
    else:
        descuento = 0
    precio_con_descuento = precio_sin_descuento * (1 - descuento)
    print(f"El precio total de la compra es: {precio_con_descuento} con descuento de {descuento}")

def ejercicio06():
    pass
def ejercicio07():
    pass
def ejercicio08():
    pass
def ejercicio09():
    pass
def ejercicio10():
    pass
def ejercicio11():
    pass
def ejercicio12():
    pass
def ejercicio13():
    pass
def ejercicio14():
    pass
def ejercicio15():
    pass
def ejercicio16():
    pass
def ejercicio17():
    pass
def ejercicio18():
    pass
def ejercicio19():
    pass
def ejercicio20():
    pass
def ejercicio21():
    pass
def ejercicio22():
    pass
def ejercicio23():
    pass
def ejercicio24():
    pass
def ejercicio25():
    pass
def ejercicio26():
    pass
def ejercicio27():
    pass
def ejercicio28():
    pass
def ejercicio29():
    pass
def ejercicio30():
    pass
def ejercicio31():
    pass
def ejercicio32():
    pass
def ejercicio33():
    pass
def ejercicio34():
    pass
def ejercicio35():
    pass
def ejercicio36():
    pass
def ejercicio37():
    pass
def ejercicio38():
    pass
def ejercicio39():
    pass
def ejercicio40():
    pass