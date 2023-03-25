def ejercicio01():
    # 1. Hacer un programa en Python que lea un número por el teclado y determinar si tiene tres dígitos
    n = int(input("Ingresa un numero: "))

    if (n > 99 and n < 1000) or (n < -99 and n > -1000):
        print(f"El numero {n} es de 3 digitos")
    else:
        print(f"El numero {n} no es de 3 digitos")

def ejercicio02():
    # 2. Hacer un programa en Python que lea un número entero por el teclado y determinar si es negativo.
    n = None
    while n is None:
        try:
            n = int(input("Ingrese un número entero: "))
            if (n < 0):
                print(f"El número {n} es negativo")
            else:
                print(f"El número {n} es positivo")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio03():
    # 3. Hacer un programa en Python que lea un número y determinar si termina en 4.
    numero = int(input("Ingrese un número: "))
    if numero % 10 == 4:
        print("El número termina en 4.")
    else:
        print("El número no termina en 4.")

def ejercicio04():
    # 4. Hacer un programa en Python que lea tres números enteros y los muestre de menor a mayor.
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
     # 5. Hacer un programa en Python para una tienda de zapatos que tiene una promoción
     # de descuento para vender al mayor, esta dependerá del número de zapatos que se
     # compren. Si son más de diez, se les dará un 10% de descuento sobre el total de la
     # compra; si el número de zapatos es mayor de veinte pero menor de treinta, se le
     # otorga un 20% de descuento; y si son más treinta zapatos se otorgará un 40% de
     # descuento. El precio de cada zapato es de $80.
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
    # 6. Hacer un programa en Python para ayudar a un trabajador a saber cuál será
    #su sueldo semanal, se sabe que si trabaja 40 horas o menos, se le pagará $20
    #por hora, pero si trabaja más de 40 horas entonces las horas extras se le
    #pagarán a $25 por hora. 
    normalPrice = 20
    extraPrice = 25
    hours = None
    while hours is None:
        try:
            hours = int(input("Ingrese número de horas trabajadas: "))
            if hours <= 40:
                print(f"Pagar s/{(hours * normalPrice)}")
            elif hours > 40:
                extraHour = hours - 40
                print(f"Pagar s/{40*normalPrice + extraHour*extraPrice}")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio07():
    #7. Hacer un programa en Python para una tienda de helado que da un descuento
    #por compra a sus clientes con membresía dependiendo de su tipo, sólo existen tres
    #tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:
    #    Tipo A 10% de descuento
    #    Tipo B 15% de descuento
    #   Tipo C 20% de descuento    

    price = float(input("Ingrese precio de helado: "))
    option = input("Ingrese tipo membresía A, B o C: ").strip().lower()

    if option == "a":
        finalPrice = price - price * 0.1
        print(f"Precio final con 10% dcto: s/{finalPrice}")
    elif option == "b":
        finalPrice = price - price * 0.15
        print(f"Precio final con 15% dcto: s/{finalPrice}")
    elif option == "c":
        finalPrice = price - price * 0.2
        print(f"Precio final con 20% dcto: s/{finalPrice}")
    else:
        print(f"Opción no válida")


def ejercicio08():
    #  8. Hacer un programa en Python para calcular el promedio de tres notas
    #  y determinar si el estudiante aprobó o no.
    grade1 = grade2 = grade3 = None
    while grade1 is None or grade2 is None or grade3 is None:
        try:
            grade1 = float(input("Ingresar nota 1: "))
            grade2 = float(input("Ingresar nota 2: "))
            grade3 = float(input("Ingresar nota 3: "))

            media = (grade1 + grade2 + grade3) / 3
            if media < 14:
                print(f"DESAPROBADO, promedio: {media}")
            elif media >= 14:
                print(f"APROBADO, promedio: {media}")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio09():
    # 9. Hacer un programa en Python para determinar el aumento de un trabajador,
    #se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%,
    #si generaba menos de $2000 su aumento será de un 10%.'''
    salary = None
    while salary is None:
        try:
            salary = float(input("Ingresar sueldo del trabajador: "))

            if salary > 2000:
                newSalary = salary + salary*0.05
                print(f"Nuevo sueldo: s/{newSalary}")
            else:
                newSalary = salary + salary*0.1
                print(f"Nuevo sueldo: s/{newSalary}")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio10():
    # 10. Hacer un programa en Python que diga si un número es par o impar.
    n = int(input("Ingrese un numero: "))

    if(n%2 == 0):
        print(f"El numero {n} es Par")
    else:
        print(f"El numero {n} es Impar")


def ejercicio11():
    # 11. Hacer un programa en Python que lea tres números y diga cuál es el mayor.
    print('ingrese 3 numeros: ')
    n1 = int(input('número 1: '))
    n2 = int(input('número 2: '))
    n3 = int(input('número 3: '))
    numeros = [n1,n2,n3]
    maximo = max(numeros)
    print(f'el mayor número es {maximo}')


def ejercicio12():
    # 12. Hacer un programa en Python que lea dos números y diga cuál es el mayor.
    n1 = int(input("primer numero: "))
    n2 = int(input("segundo numero: "))

    if(n1 > n2):
        print(f"El mayor es: {n1}")
    else:
        print(f"El mayor es: {n2}")


def ejercicio13():
    # 13. Hacer un programa en Python que lea una letra y diga si es una vocal.
    letter = input("Ingresa una letra: ").strip().lower()
    if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        print(f"la letra {letter} es una vocal")
    else:
        print(f"{letter} No es una vocal")


def ejercicio14():
    # 14. Hacer un programa en Python que lea un entero positivo
    # del 1 al diez y al 9 y determine si es un número primo.
    num = None
    while num is None:
        try:
            num = int(input("Ingresa un número de 1 al 10: "))
            count = 0

            if num > 10:
                print(f"Debe ingresar un número de 1 a 10")
            else:
                for i in range(1, 10):
                    if num % i == 0:
                        count = count + 1
                if count == 2:
                    print(f"{num} es número primo")
                else:
                    print(f"{num} No es número primo")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio15():
    # 15. Hacer un programa en Python que convierta centímetros a pulgadas y libras a kilogramos.
    print(f"Selecciona opción 1 o 2:")
    print(f"1: Centímetros a pulgadas")
    print(f"2: Libras a kilogramos")

    option = int(input("Ingresa opción: "))

    if option == 1:
        num = float(input("Ingresar valor: "))
        print(f"{num} cm es igual a {num / 2.54} pulgadas")
    elif option == 2:
        num = float(input("Ingresar valor: "))
        print(f"{num} libras es igual a {num / 2.205} kg")
    else:
        print(f"Opción no válida")


def ejercicio16():
    # 16. Hacer un programa en Python que lea un número y según ese número, indique el día que corresponde.
    num = None
    while num is None:
        try:
            num = int(input("Ingresar número de día: "))

            if num == 1:
                print(f"{num} es Domingo")
            elif num == 2:
                print(f"{num} es Lunes")
            elif num == 3:
                print(f"{num} es Martes")
            elif num == 4:
                print(f"{num} es Miércoles")
            elif num == 5:
                print(f"{num} es Jueves")
            elif num == 6:
                print(f"{num} es Viernes")
            elif num == 7:
                print(f"{num} es Sábado")
            else:
                print(f"Opción no válida")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio17():
    # 17. Hacer un programa en Python donde se ingrese una hora y nos calcule la hora dentro de un segundo.
    h = m = s = None
    while h is None or m is None or s is None:
        try:
            print(f"Ingresar hora - minuto - segundo")
            h = int(input("Hora: "))
            m = int(input("Minuto: "))
            s = int(input("Segundo: "))

            if (h < 24 and m < 60 and s < 60):
                s = s + 1
                if s == 60:
                    s = 0
                    m = m + 1
                    if m == 60:
                        m = 0
                        h = h + 1
                        if h == 24:
                            h = 0
                print(
                    f"La hora dentro de un segundo será: {h}:{m}:{s}")
            else:
                print(f"Debe ingresar valores correctos")

        except ValueError:
            print(f"Ingresa solo números")


def ejercicio18():
    #18. Hacer un programa en Python para una empresa se encarga de la venta y
    #distribución de CD vírgenes. Los clientes pueden adquirir los artículos
    #(supongamos un único producto de una única marca) por cantidad. Los precios son:
    #$10. Si se compran unidades separadas hasta 9.
    #$8. Si se compran entre 10 unidades hasta 99.
    #$7. Entre 100 y 499 unidades.
    #$6. Para mas de 500 unidades.
    #La ganancia para el vendedor es de 8,25% de la venta. Realizar un algoritmo
    #en Pseint que dado un número de CDs a vender calcule el precio total para el
    #cliente y la ganancia para el vendedor.

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
    #19. Hacer un programa en Python para una heladería se tienen 4 tipos de
    # empleados ordenados de la siguiente forma con su número identificador y
    # salario diario correspondiente:
    #1: Cajero(56$/ día).
    #2: Servidor(64$/ día).
    #3: Preparador de mezclas(80$/ día).
    #4: Mantenimiento(48$/ día).
    #El dueño de la tienda desea tener un programa donde sólo ingrese dos números
    #enteros que representen al número identificador del empleado y la cantidad de días
    #que trabajó en la semana(6 días máximos). Y el programa le mostrará por pantalla la
    #cantidad de dinero que el dueño le debe pagar al empleado que ingresó.

    id = input("Ingresar identificador de empleado (ejemplo: 01): ")

    if len(id) == 2:
        days = int(input("Ingresar numero de días trabajados: "))
        if days <= 6:
            if id == "01":
                print(f"Total a pagar al Cajero por {days} días: s/{days*56}")
            elif id == "02":
                print(
                    f"Total a pagar al Servidor por {days} días: s/{days*64}")
            elif id == "03":
                print(
                    f"Total a pagar al Preparador por {days} días: s/{days*80}")
            elif id == "04":
                print(
                    f"Total a pagar al Mantenimiento por {days} días: s/{days*48}")
            else:
                print(f"Identificador incorrecto")
        else:
            print(f"Numero de días debe ser igual o menor a 6")
    else:
        print(f"Identificador incorrecto")


def ejercicio20():
    #20. Hacer un programa en Python que que lea 4 números enteros positivos
    #y verifique y realice las siguientes operaciones:
    #1.- ¿Cuántos números son Pares?
    #2.- ¿Cuál es el mayor de todos?
    #3.- Si el tercero es par, calcular el cuadrado del segundo.
    #4.- Si el primero es menor que el cuarto, calcular la media de los 4 números.
    #5.- Si el segundo es mayor que el tercero, verificar si el tercero esta comprendido
    #entre los valores 50 y 700. Si cumple se cumple la segunda condición,
    #calcular la suma de los 4 números.

    n1 = int(input("ingrese n1: "))
    n2 = int(input("ingrese n2: "))
    n3 = int(input("ingrese n3: "))
    n4 = int(input("ingrese n4: "))

    def cp(n):
        contador = 0
        if (n % 2 == 0):
            contador = contador + 1
        return contador

    print("Cantidad de numeros pares:")
    contadorT = cp(n1) + cp(n2) + cp(n3) + cp(n4)
    print(f"Hay {contadorT} pares")

    if (n1 > 2 and n1 > n3 and n1 > n4):
        print(f"El numero mayor es el {n1}")
    elif (n2 > n1 and n2 > n3 and n2 > n4):
        print(f"El numero mayor es el {n2}")
    elif (n3 > n1 and n3 > n2 and n3 > n4):
        print(f"El numero mayor es el {n3}")
    else:
        print(f"El numero mayor es el {n4}")

    if(n3 % 2 == 0):
        print(f"Cuadrado del 2do: {n2 * n2}")
    if(n1 < n4):
        print(f"La media de los 4 es: {(n1 + n2 + n3 + n4) / 4}")
    if(n2 > n3):
        if(n3 > 49 and n3 < 700):
            print(f"La suma de los 4 numeros es:  {(n1 + n2 + n3 + n4)}")

def ejercicio21():
   # 21. Hacer un programa en Python que permita calcular el factorial de un número.
     num = int()	
     contador = int()	
     factorial = int()	
     print("Digite un numero entero:")	
     num = int(input())	
     contador = 1	
     factorial = 1	
     for contador in range(1,num+1):	
        factorial = factorial*contador
	print("El factorial del numero ingresado es: ",factorial)

def ejercicio22():
    # 22. Hacer un programa en Python para calcular la suma de los n primeros números.
    n = int(input("Ingrese el valor de n: "))
    suma = n*(n+1)/2
    print("La suma de los", n, "primeros números es", suma)


def ejercicio23():
    # 23. Hacer un programa en Python para calcular la suma de los
    # números impares menores o iguales a n.
    sum = 0
    num = None
    while num is None:
        try:
            num = int(input("Ingresa un número entero positivo: "))

            for i in range(1, num + 1, 2):
                sum += i
            print(
                f"La suma de los números impares menores o iguales a {num} es: {sum}")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio24():
    # 24. Hacer un programa en Python para realizar la suma de todos
    #  los números pares hasta el 1000.
    sum = 0
    i = 1
    while i <= 1000:
        if i % 2 == 0:
            sum += i
        i += 1
    print(f"La suma de los números pares hasta 1000 es: {sum}")


def ejercicio25():
    # 25. Hacer un programa en Python para calcular el factorial de un número de una forma distinta.
    num = None
    while num is None:
        try:
            num = int(input("Ingresa un número para calcular el fatorial: "))

            if num <= 0:
                print(f"Ingresa un número positivo o mayor a cero")
            else:
                factorial = 1
                for i in range(1, num + 1, 1):
                    factorial = factorial * i
                print(f"El factorial de {num} es: {factorial}")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio26():
    # 26. Hacer un programa en Python para calcular el resto y cociente
    # por medio de restas sucesivas.
    num1 = num2 = None
    while num1 is None or num2 is None:
        try:
            num1 = int(input("Ingresa primer número: "))
            num2 = int(input("Ingresa segundo número: "))

            cociente = 0
            while num1 >= num2:
                num1 = num1 - num2
                cociente += 1
            print(f"El cociente es: {cociente}")
            print(f"El resto es : {num1}")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio27():
    # 27. Hacer un programa en Python para determinar la media de una lista indefinida
    # de números positivos, se debe acabar el programa al ingresar un número negativo.
    i = 1
    count = 0
    sum = 0

    while i >= 0:
        i = int(input("Ingresa un número positivo: "))
        if i >= 0:
            sum = sum + i
            count += 1
    if count > 0:
        print(f"La media de los números positivos es: {sum / count}")


def ejercicio28():
    # 28. Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo repetir.
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    print(f"La suma de los primeros cien números es: {sum}")


def ejercicio29():
    # 29. Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo mientras.
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    print(f"(ciclo while) La suma de los primeros cien números es: {sum}")


def ejercicio30():
    # 30. Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo para.
    sum = 0
    for i in range(1, 101, 1):
        sum += i
    print(f"(ciclo for) La suma de los primeros cien números es: {sum}")


def ejercicio31():
    # 31. Hacer un programa en Python parar calcular la media de los números
    #  pares e impares, sólo se ingresará diez números.
    array = [int() for ind0 in range(10)]

    parSum = 0
    parCount = 0
    imparSum = 0
    imparCount = 0

    for i in range(1, 11):
        try:
            array[i-1] = int(input("Ingresa un número: "))

            if array[i-1] % 2 == 0:
                parSum = parSum + array[i-1]
                parCount += 1
            else:
                imparSum = imparSum + array[i-1]
                imparCount += 1
        except ValueError:
            print(f"Ingresa solo números")

    if parCount > 0:
        print(f"Media de pares: {parSum / parCount}")
    if imparCount > 0:
        print(f"Media de impares: {imparSum / imparCount}")


def ejercicio32():
    # 32. Se quiere saber cuál es la ciudad con la población de más personas,
    #son tres provincias y once ciudades, Hacer un programa en Python que nos
    #permita saber eso. Datos de Lambayeque, Lima, Loreto
    lima = 8500000
    lambayeque = 58276
    loreto = 883510
    print(f"Ciudad con mayor población: Lima = {lima}")


def ejercicio33():
    # 33. Hacer un programa en Python que permita al usuario continuar con el programa.
    answer = ""
    while answer != "no":
        print(f"El programa seguirá ejecutandose...")
        answer = str(input("¿Continuar? Escribir si o no: ")).strip().lower()
    print(f"El programa se cerrará")


def ejercicio34():
    # 34. Hacer un programa en Python que imprima la tabla de multiplicar de los números del uno nueve.
    for i in range(1, 10, 1): 
        print(f"Tabla de multiplicar del: {i}")
        for j in range(1, 13, 1):
            result = i * j
            print(f"{i} x {j} = {result}")


def ejercicio35():
   # 35. Hacer un programa en Python que nos permita saber cuál es el número mayor y menor, se debe ingresar sólo veinte números.
    ns = [int() for ind0 in range(20)]

    for i in range(1, 21):
        ns[i-1] = int(input(f"{i} Ingresa un número entero:"))
        bigger = ns[0]
        minor = ns[0]

        for i in range(1, 21):
            if ns[i-1] > bigger:
                bigger = ns[i-1]
            if ns[i-1] < minor:
                minor = ns[i-1]

    print(f"Número mayor: {bigger}")
    print(f"Número menor: {minor}")


def ejercicio36():
    # 36. Hacer un programa en Python para calcular la serie de Fibonacci.
    n = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
    a, b = 0, 1
    contador = 0

    while contador < n:
        print(a)
        a, b = b, a+b
        contador += 1


def ejercicio37():
    # 37. Hacer un programa en Python para conseguir el M.C.D de un número por medio del algoritmo de Euclides.
    a = 12392
    b = 870
    aux = 0
    print("Ingresar Dos Numeros")
    numero1 = int(input("Numero Uno "))
    numero2 = int(input("Numero Dos "))
    if (a < b):
        aux = a
        a = b
    while (b != 0):
        resto = a % b
        a = b
        b= resto
    print(f"Resultado Final: {a}")


def ejercicio38():
    # 38. Hacer un programa en Python que nos permita saber si un número es un número perfecto.
    acum = 0
    num = None
    while num is None:
        try:
            num = int(input("Ingresa un número para saber si es perfecto: "))

            for i in range(1, num - 1, 1):
                if num % i == 0:
                    acum = acum + i
            if num == acum:
                print(f"{num} es perfecto")
            else:
                print(f"{num} No es perfecto")
        except ValueError:
            print(f"Ingresa solo números")


def ejercicio39():
    #  39. Hacer un programa en Python que cumpla con la aproximación del número pi con
    #  la serie de Gregory-Leibniz. La formula que se debe aplicar es:
    #  Pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
    n = int(input("Ingrese el número de términos para aproximar pi: "))

    pi = 0
    for i in range(n):
        termino = 4/((2*i)+1)
        if i % 2 == 0:
            pi += termino
        else:
            pi -= termino

    print("La aproximación de pi con", n, "términos es:", pi)


def ejercicio40():
    # 40. Hacer un programa en Python que cumpla con la aproximación del número pi con la serie de Nilakantha.
    #  La formula que se debe aplicar es:
    #     Pi = = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14)...
    n = int(input("Ingrese el número de términos para aproximar pi: "))

    pi = 3
    denominador = 2
    signo = 1
    for i in range(n):
	termino = 4/(denominador*(denominador+1)*(denominador+2))
	pi += signo*termino
	denominador += 2
	signo *= -1

    print("La aproximación de pi con", n, "términos es:", pi)
