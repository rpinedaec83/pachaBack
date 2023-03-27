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
    rango_dias=[1,2,3,4,5,6,7]
    dias_diccionario = {1:'lunes',2:'martes',3:'miércoles',4:'jueves',5:'viernes',6:'sábado',7:'domingo'}
    dia = int(input('ingrese el número de día: '))
    if dia in rango_dias:
        print(f'dia {dia} corresponde a {dias_diccionario[dia]}')
    else:
        print('número de día no válido')
def ejercicio17():
    hora = input("Ingrese la hora en formato HH:MM:SS: ")
    horas, minutos, segundos = map(int, hora.split(':'))
    segundos += 1

    if segundos == 60:
        segundos = 0
        minutos += 1
        if minutos == 60:
            minutos = 0
            horas += 1
            if horas == 24:
                horas = 0

    nueva_hora = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    print("La hora después de un segundo es:", nueva_hora)
def ejercicio18():
    precio = 0
    cantidad = int(input("Ingrese la cantidad de CD vírgenes a comprar: "))
    if cantidad < 10:
        precio = cantidad * 10
    elif 10 <= cantidad & cantidad < 100:
        precio = cantidad * 8
    elif 100 <=cantidad & cantidad < 500:
        precio = cantidad * 7
    else:
        precio = cantidad * 6
    print(f"El precio a pagar por {cantidad} CD vírgenes es de ${precio}.")
def ejercicio19():
    salarios = {56: "Cajero", 64: "Servidor", 80: "Preparador de mezclas", 48: "Mantenimiento"}
    lista_identificador = [56,64,80,48]
    identificador = int(input("Ingrese el número sueldo identificador del empleado: "))
    dias_trabajados = int(input("Ingrese la cantidad de días que trabajó en la semana: "))
    
    if identificador in lista_identificador:
        salario_diario = identificador
        salario_semanal = dias_trabajados * salario_diario
        print(f"El empleado {salarios[identificador]} (${salario_diario} por día) trabajó {dias_trabajados} días y debe recibir ${salario_semanal}.")
    else:
        print(f"No existe un empleado con el sueldo identificador {identificador}.")

def ejercicio20():
    numeros = []

    for i in range(4):
        num = int(input("Ingrese un número entero positivo: "))
        numeros.append(num)

    pares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1

    mayor = max(numeros)

    if numeros[2] % 2 == 0:
        segundo_cuadrado = numeros[1] ** 2
    else:
        segundo_cuadrado = None

    if numeros[0] < numeros[3]:
        media = sum(numeros) / 4
    else:
        media = None

    if numeros[1] > numeros[2] and 50 <= numeros[2] <= 700:
        suma = sum(numeros)
    else:
        suma = None


    print("Cantidad de números pares:", pares)
    print("Mayor número:", mayor)
    print("Segundo número al cuadrado si el tercero es par:", segundo_cuadrado)
    print("Media de los cuatro números si el primero es menor que el cuarto:", media)
    print("Suma de los cuatro números si el segundo es mayor que el tercero y este está entre 50 y 700:", suma)
def ejercicio21():
    num = int(input("Ingrese un número entero: "))

    factorial = 1

    if num < 0:
        print("El factorial no está definido para números negativos.")
    elif num == 0:
        print("El factorial de 0 es 1.")
    else:
        for i in range(1, num+1):
            factorial *= i
        print("El factorial de", num, "es", factorial)
def ejercicio22():
    n = int(input("Ingrese el valor de n: "))
    suma = n*(n+1)/2
    print("La suma de los", n, "primeros números es", suma)
def ejercicio23():
    n = int(input("Ingrese el valor de n: "))
    suma = 0
    for i in range(1, n+1, 2):
        suma += i
    print("La suma de los números impares menores o iguales a", n, "es", suma)
def ejercicio24():
    suma = 0
    for i in range(0, 1001, 2):
        suma += i

    print("La suma de todos los números pares hasta el 1000 es:", suma)
def ejercicio25():
    n = int(input("Introduce un número: "))
    if n >=0:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i

        print("El factorial de", n, "es", factorial)
    else:
        print('no está definido el factorial de números negativos')
def ejercicio26():
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))

    cociente = 0
    resto = 0

    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1

    resto = dividendo

    print("Cociente:", cociente)
    print("Resto:", resto)

def ejercicio27():
    numeros = []
    numero = int(input("Ingrese un número positivo (o negativo para terminar): "))
    while numero >= 0:
        numeros.append(numero)
        numero = int(input("Ingrese un número positivo (o negativo para terminar): "))

    if len(numeros) > 0:
        media = sum(numeros) / len(numeros)
        print("La media es:", media)
    else:
        print("No se ingresaron números positivos.")

def ejercicio28():
    suma = 0
    for i in range(1, 101):
        suma += i
    print("La suma de los primeros cien números es:", suma)
def ejercicio29():
    suma = 0
    i = 1
    while i <101:
        suma += i
        i+=1
    print("La suma de los primeros cien números es:", suma)
def ejercicio30():
    suma = 0
    for i in range(1, 101):
        suma += i
    print("La suma de los primeros cien números es:", suma)
def ejercicio31():
    numeros = []
    pares = []
    impares = []

    for i in range(10):
        num = int(input("Ingrese un número: "))
        numeros.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

        if len(pares) > 0:
            media_pares = sum(pares) / len(pares)
            print("La media de los números pares es:", media_pares)
        else:
            print("No se ingresaron números pares.")

        if len(impares) > 0:
            media_impares = sum(impares) / len(impares)
            print("La media de los números impares es:", media_impares)
        else:
            print("No se ingresaron números impares.")
def ejercicio32():
    ciudades = [
        {'nombre': 'Lambayeque', 'poblacion': 60870},
        {'nombre': 'Motupe', 'poblacion': 16738 },
        {'nombre': 'Olmos', 'poblacion': 15205},
        {'nombre': 'San José', 'poblacion': 10686}, #ciudades Lambayeque
        {'nombre': 'Lima', 'poblacion': 10113318}, 
        {'nombre': 'Nauta', 'poblacion': 29963}, #ciudades Loreto
        {'nombre': 'Trompeteros', 'poblacion': 8396},
        {'nombre': 'Tigre', 'poblacion': 6448},
        {'nombre': 'Parinari', 'poblacion': 6085},
        {'nombre': 'Urarinas', 'poblacion': 11545},
        {'nombre': 'Iquitos', 'poblacion':377609}
    ]
    poblacion_maxima = 0
    ciudad_con_max_poblacion = ""
    for ciudad in ciudades:
        poblacion = ciudad['poblacion']
        if poblacion > poblacion_maxima:
            poblacion_maxima = poblacion
            ciudad_con_max_poblacion = ciudad['nombre']

    print(f"La ciudad con la población más alta es {ciudad_con_max_poblacion} con {poblacion_maxima} habitantes.")

def ejercicio33():
    continuar = True

    while continuar:
        print("Hola, ¿qué quieres hacer?")
        
        respuesta = input("¿Quieres continuar? (s/n): ")
        if respuesta == "n":
            continuar = False
def ejercicio34():
    for i in range(1, 10):
        print(f"Tabla de multiplicar del {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print("")

def ejercicio35():
    numeros = []
    for i in range(20):
        num = int(input("Ingrese un número: "))
        numeros.append(num)

    mayor = max(numeros)
    menor = min(numeros)

    print("El número mayor es:", mayor)
    print("El número menor es:", menor)
def ejercicio36():
    n = int(input("Ingrese el número de términos que desea: "))
    a, b = 0, 1
    contador = 0

    if n <= 0:
        print("Ingrese un número positivo.")
    elif n == 1:
        print("La serie de Fibonacci hasta el término",n,":")
        print(a)
    else:
        print("La serie de Fibonacci hasta el término",n,":")
        while contador < n:
            print(a)
            c = a + b
            a = b
            b = c
            contador += 1
def ejercicio37():
    num1 = abs(int(input('ingrese el primer número: ')))
    num2 = abs(int(input('ingrese el segundo número: ')))
    print("El M.C.D. de", num1, "y", num2,"es ")
    # Iteramos mientras el segundo número sea diferente de cero
    while num2:
        # Realizamos la división entera y obtenemos el resto
        num1, num2 = num2, num1 % num2
    
    # El M.C.D. es el último divisor no nulo
    mcd= num1
    print(mcd)
def ejercicio38():
    def es_perfecto(numero):
        suma = 0
        for divisor in range(1, numero):
            if numero % divisor == 0:
                suma += divisor
        return suma == numero

    numero = int(input("Ingrese un número: "))
    if es_perfecto(numero):
        print(numero, "es un número perfecto")
    else:
        print(numero, "no es un número perfecto")
def ejercicio39():
    def approx_Leibniz(num_terms):
        pi_approx = 0
        sign = 1
        for i in range(1, num_terms * 2, 2):
            pi_approx += sign * (1 / i)
            sign = -sign
        return pi_approx * 4
    pi_approx = approx_Leibniz(100)
    print(pi_approx)
def ejercicio40():
    def nilakantha_pi(n):
        pi = 3
        sign = 1
        denom = 2
        for i in range(n):
            term = 4/(denom * (denom + 1) * (denom + 2))
            pi += sign * term
            sign *= -1
            denom += 2
        return pi

    n_terms = int(input("Ingrese el número de términos para calcular pi: "))
    pi_approx = nilakantha_pi(n_terms)
    print(f"La aproximación de pi con {n_terms} términos es: {pi_approx}")