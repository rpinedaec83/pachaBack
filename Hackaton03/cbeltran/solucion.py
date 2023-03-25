
def ejercicio01():
    """Hacer un programa en Python que lea un número por el teclado y determinar si tiene tres dígitos"""
    print("\nPrograma -> Determinar 3 dígitos")
    numero = input("Ingrese un número: ")
    if len(numero) == 3:
        print("El número tiene", numero,"tres dígitos")
    else:
        print("El número", numero, "no tiene tres dígitos")

    
def ejercicio02():
    """Hacer un programa en Python que lea un número entero por el teclado y determinar si es negativo."""
    numero = int(input("Ingrese un número: "))
    if numero < 0 :
        print(f"El número",numero,"es negativo")
    else:
        print("El número", numero, "no es negativo")


def ejercicio03():
    """Hacer un programa en Python que lea un número y determinar si termina en 4."""
    numero = int(input('Ingrese un número: '))

    if numero % 10 == 4 :
        print("El número", numero, "termina en 4.")
    else:
        print("El número", numero, "no termina en 4")


def ejercicio04():
    """Hacer un programa en Python que lea tres números enteros y los muestre de menor a mayor."""

    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))

    menor = min(num1, num2, num3)
    mayor = max(num1, num2, num3)
    medio = num1 + num2 + num3 - menor - mayor

    print ("Los números ordenados de menor a mayor son:", menor, medio, mayor)


def ejercicio05():
    """Hacer un programa en Python para una tienda de zapatos que tiene una promoción de descuento para vender al mayor,
    #esta dependerá del número de zapatos que se compren. Si son más de diez, se les dará un 10% de descuento sobre el total de la compra;
    #si el número de zapatos es mayor de veinte pero menor de treinta, se le otorga un 20% de descuento; y si son más treinta zapatos 
    #se otorgará un 40% de descuento. El precio de cada zapato es de $80."""

    cantidadZapatos= int(input("Ingrese la cantidad de zapatos: "))
    precioTotal = cantidadZapatos * 80
    if cantidadZapatos > 30:
        descuento = 40
    elif cantidadZapatos > 20:
        descuento = 20
    elif cantidadZapatos > 10:
        descuento = 10
    else:
        descuento = 0

    precioConDescuento = precioTotal - ( precioTotal * descuento / 100)
    print ("\nEl precio total de los zapatos es: $" + str(precioTotal) +
        "\nSe aplica un descuendo de: " + str(descuento) + "%" +        
        "\nEl precio con descuento es: $" + str(precioConDescuento))


def ejercicio06():
    """Hacer un programa en Python para ayudar a un trabajador a saber cuál será su sueldo semanal
    se sabe que si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas
    entonces las horas extras se le pagarán a $25 por hora."""

    horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
    sueldoExtra = 0
    horasExtra= 0
    if horasTrabajadas <= 40:
        sueldoSemanal = horasTrabajadas * 20
    else:
        horasExtra = horasTrabajadas - 40
        sueldoExtra = horasExtra * 25
        sueldoSemanal = (40 * 20) + sueldoExtra

    print ("\nHoras trabajadas: " + str(horasTrabajadas) + 
        "\nHoras extra: "+ str(horasExtra) + 
        "\nPago por horas extra: $" + str(sueldoExtra) +
        "\nEl sueldo semanal es: $" + str(sueldoSemanal)) 


def ejercicio07():
    """Hacer un programa en Python para una tienda de helado que da un descuento por compra a sus clientes con membresía 
    dependiendo de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:
    Tipo A 10% de descuento
    Tipo B 15% de descuento
    Tipo C 20% de descuento"""

    descuentos = {"A": 0.1, "B": 0.15, "C": 0.2}
    tipoMembresia = input("Ingrese el tipo de membresía ('A', 'B' o 'C'): ")

    if tipoMembresia in descuentos:
        pago = float(input("Ingrese el monto de su compra: "))
        descuento = pago * descuentos[tipoMembresia]
        pagoConDescuento = pago - descuento
        print("Descuento aplicado:", descuento)
        print("Pago a realizar con descuento:", pagoConDescuento)
    else:
        print("Tipo de membresía no válido. Por favor ingrese 'A', 'B' o 'C'.")      

def ejercicio08():
    """Hacer un programa en Python para calcular el promedio de tres notas y determinar si el estudiante aprobó o no."""

    nota1=int(input("Ingrese la primera nota: "))
    nota2=int(input("Ingrese la segunda nota: "))
    nota3=int(input("Ingrese la tercera nota: "))

    promedio = (nota1 + nota2 + nota3) / 3
    if promedio < 13:
        print("El promedio de las 3 notas es:",promedio,"\n---> El estudiante desaprobó :( <---")
    else:
        print("El promedio de las 3 notas es:",promedio,"\n---> El estudiante aprobó :D <---")  


def ejercicio09():
    """Hacer un programa en Python para determinar el aumento de un trabajador, 
    se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%, 
    si generaba menos de $2000 su aumento será de un 10%."""

    salario = int(input("Ingrese el sueldo: "))

    if salario < 2000:
        print("Recibe un aumento de 10%, su nuevo salario es:",salario + (salario * 0.1))
    else:
        print("Recibe un aumento de 5%, su nuevo salario es:",salario + (salario * 0.05))


def ejercicio10():

    """Hacer un programa en Python que diga si un número es par o impar."""

    numero=int(input("Ingrese un número: "))

    if numero % 2 == 0:
        print("El número",numero,"es par")
    else:
        print("El número",numero,"es impar")


def ejercicio11():
    """Hacer un programa en Python que lea tres números y diga cuál es el mayor."""

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el primer número: "))
    num3 = int(input("Ingrese el primer número: "))

    print("El número mayor es:", max(num1, num2, num3))

def ejercicio12():
    """Hacer un programa en Python que lea 2 números y diga cuál es el mayor."""

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el primer número: "))

    print("El número mayor es:", max(num1, num2))


def ejercicio13():
    """Hacer un programa en Python que lea una letra y diga si es una vocal."""

    vocales = ["A","E","I","O","U"]
    letra = input("Ingrese una letra en mayúscula: ")

    for vocal in vocales:  
        if letra == vocal:
            print("La letra:", letra,"es una vocal")
            break
    else:
        print("La letra:", letra, "no es una vocal")


def ejercicio14():
    """Hacer un programa en Python que lea un entero positivo del 1 al diez y al 9 y determine si es un número primo."""

    numero = int(input("Ingrese un número del 1 al 9: "))
    numerosPrimos = (2, 3, 5, 7)
    if numero < 10 and numero > 0:
        for i in numerosPrimos:
            if numero == i:
                print("El número", numero,"es un número primo")
                break
        else:
            print("El número", numero,"no es un número primo")
    else:
        print("El número que ingresó no es un número del 1 al 9")


def ejercicio15():
    """Hacer un programa en Python que convierta centímetros a pulgadas y libras a kilogramos."""

    tipoUnidad = input("\nDigíte 1 para convertir libras a kilogramos \nDigíte 2 para convertir centímetros a pulgadas --> ")
    valor = float(input("Ingrese el valor numérico a convertir: "))

    unidades = {"1":valor * ( 1 / 2.21), "2":valor / 2.54}
    if tipoUnidad == "1":
        print( f'{valor} libra(s) equivale a ', unidades["1"], "kilogramo(s)")
    elif tipoUnidad == "2":
        print( f'{valor} centimero(s) equivale a ', unidades["2"], "pulgada(s)")
    else:
        print("Dígito o valor incorrecto")

def ejercicio16():
    """Hacer un programa en Python que lea un número y según ese número, indique el día que corresponde."""
    
    dias = {"1":"LUNES", "2":"MARTES" ,"3":"MIÉRCOLES" ,"4":"SÁBADO" ,"5":"DOMINGO"}
    numero = input("Ingrese un número: ")
    if numero in dias:
        print("Al número:", numero,"le corresponde el día:",dias[numero])
    else:
        print("Al número:", numero,"no le corresponde ningun día")


def ejercicio17():

    horaIngresada = input("Ingrese la hora en formato HH:MM:SS: ")
    hora, minuto, segundo = map(int, horaIngresada.split(":"))

    segundo = segundo + 1
    if segundo == 60:
        segundo = "00"
        minuto = minuto + 1
        if minuto == 60:
            minuto = "00"
            hora = hora + 1
            if hora == 24:
                hora = "00"

    print("La nueva hora es: " + str(hora) + ":" + str(minuto) + ":" + str(segundo))

def ejercicio18():
    """Hacer un programa en Python para una empresa se encarga de la venta y distribución de CD vírgenes. 
    Los clientes pueden adquirir los artículos por cantidad. Los precios son:
    $10. Si se compran unidades separadas hasta 9.
    $8. Si se compran entre 10 unidades hasta 99.
    $7. Entre 100 y 499 unidades.
    $6. Para mas de 500 unidades.
    La ganancia para el vendedor es de 8,25 % de la venta. 
    Realizar un programa en Python que dado un número de CDs a vender 
    calcule el precio total para el cliente y la ganancia para el vendedor."""

    cantidadCD = int(input("Ingrese la cantidad de CD's a comprar: "))

    if cantidadCD <= 9:
        ventaTotal = cantidadCD * 10
    elif cantidadCD <= 99 and cantidadCD >= 10:
        ventaTotal = cantidadCD * 8
    elif cantidadCD <= 499:
        ventaTotal = cantidadCD * 7
    else:
        ventaTotal = cantidadCD * 6

    gananciaVendedor = ventaTotal * 0.0825

    print("Precio total a pagar por el cliente: $" + str(ventaTotal) + 
        "\nGanancia del vendedor:$", float(f'{gananciaVendedor:.2f}'))
    
def ejercicio19():
    """Hacer un Programa en Pyhton para una heladería se tienen 4 tipos de empleados ordenados de la siguiente forma
    con su número identificador y salario diario correspondiente:
    Cajero (56$/día).
    Servidor (64$/día).
    Preparador de mezclas (80$/día).
    Mantenimiento (48$/día).
    El dueño de la tienda desea tener un programa donde sólo ingrese dos números enteros
    que representen al número identificador del empleado y la cantidad de días que trabajó en la semana (6 días máximos).
    Y el programa le mostrará por pantalla la cantidad de dinero que el dueño le debe pagar al empleado que ingresó"""
    
    idEmpleado = (input("Ingrese el identificador del empleado:"
                    "\n1: Cajero \n2: Servidor \n3: Preparador \n4: Mantenimiento\n--> " ))
    diasTrabajados = int(input("Ingrese la cantidad de días trabajados:\n--> "))
    pagoTrabajador={"1":56 * diasTrabajados, "2":64 * diasTrabajados, "3":80 * diasTrabajados, "4":48 * diasTrabajados}

    if diasTrabajados < 7:
        if idEmpleado in pagoTrabajador:
            sueldo = pagoTrabajador[idEmpleado];
            print("El suendo es: $"+ str(sueldo))
    else:
        print("Los días trabajados son mayores a 6. Intente otra vez.")
        

def ejercicio20():
    """Hacer un programa en Python que que lea 4 números enteros positivos y verifique y realice las siguientes operaciones:
    ¿Cuántos números son Pares?
    ¿Cuál es el mayor de todos?
    Si el tercero es par, calcular el cuadrado del segundo.
    Si el primero es menor que el cuarto, calcular la media de los 4 números.
    Si el segundo es mayor que el tercero, verificar si el tercero esta comprendido entre los valores 50 y 700. 
    Si cumple se cumple la segunda condición, calcular la suma de los 4 números."""

    listaNumeros = []
    for i in range(4):
        num = int(input("Ingrese un número: "))
        listaNumeros.append(num)

    cantidadPares = 0
    for num in listaNumeros:
        if num % 2 == 0:
            cantidadPares += 1
    print("\n"+ str(cantidadPares) + " números son pares.")
    print("El número",max(listaNumeros),"es el mayor de todos.")

    if listaNumeros[2] % 2 == 0:
        cuadradoSegundo = listaNumeros[1] ** 2
        print("El cuadrado del segundo es:",cuadradoSegundo)

    if listaNumeros[0] < listaNumeros[3]:
        suma = sum(listaNumeros)
        media = suma / 4
        print("La media de los 4 números es:",media)
        print("La suma de los 4 números es:",suma)

    if listaNumeros[1] > listaNumeros [2]:
        if listaNumeros[2] < 700 and listaNumeros [2] > 50:
            print("El tercer número está comprendido entre 50  y 700")
        else:
            print("El tercer número NO está comprendido entre 50  y 700")


def ejercicio21():
    """Hacer un programa en Python que permita calcular el factorial de un número."""

    numero = int(input("Ingrese un número entero positivo: "))
    factorial = 1

    if numero < 0:
        print("Lo siento, el factorial no está definido para números negativos.")
    elif numero == 0:
        print("El factorial de 0 es 1.")
    else:
        for i in range(1, numero + 1):
            factorial = factorial * i
        print("El factorial de", numero, "es", factorial)


def ejercicio22():
    """Hacer un programa en Python para calcular la suma de los n primeros números."""

    n = int(input("Ingrese un número entero positivo: "))

    suma = n * (n + 1) / 2
    print("La suma de los primeros", n, "números es", suma)

def ejercicio23():
    """Hacer un programa en Python para calcular la suma de los números impares menores o iguales a n."""

    n = int(input("Ingrese un número entero positivo: "))

    suma = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            suma += i
    print("La suma de los números impares menores o iguales a", n, "es", suma)

def ejercicio24():
    """Hacer un programa en Python para realizar la suma de todos los números pares hasta el 1000."""
    suma = 0
    for i in range(2, 1001, 2):
        suma += i
    print("La suma de todos los números pares hasta 1000 es:", suma)


def ejercicio25():
    """Hacer un programa en Python para calcular el factorial de un número de una forma distinta."""
    import math
    n = int(input("Ingrese un número entero positivo: "))
    factorial = math.factorial(n)
    print("El factorial de", n, "es", factorial)

def ejercicio26():
    """Hacer un programa en Python para calcular el resto y cociente por medio de restas sucesivas."""
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))

    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1

    resto = dividendo

    print("El cociente es:", cociente)
    print("El resto es:", resto)

def ejercicio27():
    """Hacer un programa en Python para determinar la media de una lista indefinida de números positivos, 
    se debe acabar el programa al ingresar un número positivo."""
    total = 0
    count = 0
    while True:
        try:
            num = float(input("Ingresa un número positivo (para terminar ingresa un número positivo): "))
            if num <= 0:
                break
            total += num
            count += 1
        except ValueError:
            print("Error: debes ingresar un valor numérico.")

    if count > 0:
        media = total / count
        print("La media de los números ingresados es:", media)


def ejercicio28():
    """Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo repetir.(while)"""
    suma = 0
    i = 1

    while i <= 100:
        suma += i
        i += 1

    print("La suma de los primeros 100 números es:", suma)


def ejercicio29():
    """Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo mientras(while)."""
    suma = 0
    i = 1

    while i <= 100:
        suma += i
        i += 1

    print("La suma de los primeros 100 números es:", suma)


def ejercicio30():
    """Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo para.(for)"""
    suma = 0
    for i in range(1, 101):
        suma += i

    print("La suma de los primeros 100 números es:", suma)


def ejercicio31():
    """Hacer un programa en Python parar calcular la media de los números pares e impares, sólo se ingresará diez números."""

    sumaPares = 0
    sumaImpares = 0
    contadorPares = 0
    contadorImpares = 0

    for i in range(10):
        numero = int(input("Ingresa un número: "))
        if numero % 2 == 0:
            sumaPares += numero
            contadorPares += 1
        else:
            sumaImpares += numero
            contadorImpares += 1

    if contadorPares == 0:
        mediaPares = 0
    else:
        mediaPares = sumaPares / contadorPares

    if contadorImpares == 0:
        mediaImpares = 0
    else:
        mediaImpares = sumaImpares / contadorImpares

    print("La media de los números pares es:", mediaPares)
    print("La media de los números impares es:", mediaImpares)


def ejercicio32():
    """Se quiere saber cuál es la ciudad con la población de más personas, son tres provincias y once ciudades,
    Hacer un programa en Python que nos permita saber eso. Datos de Lambayeque, Lima, Loreto"""

    poblacion = {
    "Ciudad de Lima": 8500000,
    "Ciudad de Huacho": 156790,
    "Ciudad de Barranca": 158749,
    "Ciudad San Vicente de Cañete": 97882 ,
    "Ciudad de Ferreñafe": 47259,
    "Ciudad Lambayeque": 58276,
    "Ciudad Chiclayo": 552508,
    "Ciudad Pimentel": 19989,
    "Ciudad Iquitos": 377609,
    "Ciudad Yurimaguas": 34528,
    "Ciudad Requena": 25313
    }

    print("La ciudad con la población más grande es:", max(poblacion))


def ejercicio33():
    """Hacer un programa en Python que permita al usuario continuar con el programa."""
    continuar = True
    while continuar:
        opcion = input("\n¿ Desea continuar con el programa ?\nPresiona 'Enter' para continuar o escribe 'salir' para salir: ")
        if opcion.lower() == "salir":
            continuar = False
    print("Programa finalizado.")


def ejercicio34():
    """Hacer un programa en Python que imprima la tabla de multiplicar de los números del uno nueve."""
    for i in range(1, 10):  
        print(f"Tabla de multiplicar del {i}:") 
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print()


def ejercicio35():
    """Hacer un programa en Python que nos permita saber cuál es el número mayor y menor, se debe ingresar sólo veinte números."""

    numeros = []
    for i in range(20):
        numero = int(input("Ingrese el número {}: ".format(i+1)))
        numeros.append(numero)
        print("El número mayor es: ", max(numeros))


def ejercicio36():
    """Hacer un programa en Python para calcular la serie de Fibonacci."""
    fibonacci = 0
    fib1 = 0
    fib2 = 1

    n = int(input("Ingrese un numero: "))
    print("La serie de Fibonacci hasta", n, "es:")

    for i in range(1, n+1):
        print(fib1)
        fibonacci = fib1 + fib2
        fib1 = fib2
        fib2 = fibonacci


def ejercicio37():
    """Hacer un programa en Python para conseguir el M.C.D de un número por medio del algoritmo de Euclides"""
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    mcd = a
    resto = b
    while resto != 0:
        mcd = resto
        resto = a % resto
        a = mcd
    print("El MCD de", a, "y", b, "es:", mcd)


def ejercicio38():
    """Hacer un programa en Python que nos permita saber si un número es un número perfecto"""

    numero = int(input("Ingrese un número: "))
    sumaDivisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            sumaDivisores += i

    if sumaDivisores == numero:
        print(numero, "es un número perfecto")
    else:
        print(numero, "no es un número perfecto")

def ejercicio39():

    """Hacer un programa en Python que cumpla con la aproximación del número pi con la serie de Gregory-Leibniz. 
    La formula que se debe aplicar es:  Pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ..."""

    num = 0
    num_pi = 0.0
    contador = 0

    num = int(input("Ingrese un número: "))

    for i in range(1, num+1, 2):
        if contador % 2 == 0:
            num_pi += 4 / i
        else:
            num_pi -= 4 / i
        contador += 1

    print("Pi se aproxima a:", num_pi)


def ejercicio40():
    """Hacer un programa en Python que cumpla con la aproximación del número pi con la serie de Nilakantha. 
    La formula que se debe aplicar es: Pi = = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14) ..."""

    num = 0
    num_pi = 0.0
    contador = 0

    print("Ingrese un número: ")
    num = int(input())

    for i in range(2, num+1, 2):
        if contador % 2 == 0:
            num_pi += 4 / (i * (i + 1) * (i + 2))
        else:
            num_pi -= 4 / (i * (i + 1) * (i + 2))
        contador += 1

    print("Pi se aproxima a:", num_pi + 3)

