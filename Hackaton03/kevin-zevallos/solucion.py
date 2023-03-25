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
    horas_semanales = int(input('ingrese las horas trabajas en la semana: '))
    horas_extra = horas_semanales-40
    suelto_final = 0
    if horas_semanales<=40:
        sueldo_semanal = horas_semanales*25
        sueldo_adicional=horas_extra*25
        suelto_final = sueldo_semanal+sueldo_adicional
    else:
        sueldo_semanal = 40*25
        sueldo_adicional = (horas_semanales-40)*25
        suelto_final = sueldo_semanal+sueldo_adicional
    print(f'las horas trabajadas en la semana son de {horas_semanales} y el sueldo es de : {suelto_final}')
def ejercicio07():
    tipo_membresia = str(input('Ingrese el tipo de membresía: '))
    tipo_membresia = tipo_membresia.upper()
    descuento = ''
    if tipo_membresia =='A':
        descuento = '10%'
        print(f'descuento correspondiente para membresía {tipo_membresia}: {descuento} ')
    elif tipo_membresia == 'B':
        descuento = '15%'
        print(f'descuento correspondiente para membresía {tipo_membresia}: {descuento} ')
    elif tipo_membresia == 'C':
        descuento = '20%'
        print(f'descuento correspondiente para membresía {tipo_membresia}: {descuento} ')
    else:
        print('tipo de membresía no válida.')
def ejercicio08():
    nota1 = int(input('ingrese la primera nota: '))
    nota2 = int(input('ingrese la segunda nota: '))
    nota3 = int(input('ingrese la tercera nota: '))
    promedio = round((nota1+nota2+nota3)/3,ndigits=2)
    print(f'promedio: {promedio}')
    if promedio >= 10.5:
        print('el estudiante aprobó')
    else:
        print('el estudiante no aprobó')
def ejercicio09():
    sueldo= int(input('ingrese sueldo de trabajador: '))
    aumento = ''
    if sueldo >= 2000:
        aumento = '5%'
    else:
        aumento = '10%'
    print(f'el aumento correspondiente para el sueldo de {sueldo} es de : {aumento}')
def ejercicio10():
    numero = int(input('ingrese un número: '))
    if numero % 2 == 0:
        print(f'el número {numero} es par')
    else:
        print(f'el número {numero} es impar')
def ejercicio11():
    print('ingrese 3 numeros: ')
    n1 = int(input('número 1: '))
    n2 = int(input('número 2: '))
    n3 = int(input('número 3: '))
    numeros = [n1,n2,n3]
    maximo = max(numeros)
    print(f'el mayor número es {maximo}')
def ejercicio12():
    print('ingrese 2 numeros: ')
    n1 = int(input('número 1: '))
    n2 = int(input('número 2: '))
    numeros = [n1,n2]
    maximo = max(numeros)
    print(f'el mayor número es {maximo}')
def ejercicio13():
    vocales = ['a','e','i','o','u']
    letra= str(input('ingrese una letra: '))
    if letra in vocales:
        print(f'la letra {letra} es una vocal')
    else:
        print(f'la letra {letra} no es una vocal')
def ejercicio14():
    num = int(input("Ingrese un número del 1 al 10 o el 9: "))
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 9:
        print("El número", num, "es primo.")
    else:
        print("El número", num, "no es primo.")
def ejercicio15():
    centimetros=int(input('ingrese la cantidad de centímetros a convertir: '))
    libras=int(input('ingrese la cantidad de libras a convertir: '))
    pulgadas = centimetros*0.3937
    kilogramos = libras*0.4535
    print(f'{centimetros} centímetros a pulgadas : {pulgadas}')
    print(f'{libras} libras a kilogramos : {kilogramos}')
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