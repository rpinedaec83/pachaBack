def ejercicio01():
    # Hacer un programa en Python que lea un número por el teclado y determinar si tiene tres dígitos
    numero = int(input("Escribe un numero: "))
    strnumero = str(numero)
    if len(strnumero) == 3:
        print(f"Este numero tiene {len(strnumero)} digitos")
    else:
        print(
            f"Este numero no cumple con la condicion solo tiene {len(strnumero)} digitos")


def ejercicio02():
    # 2. Hacer un programa en Python que lea un número entero por el teclado y determinar si es negativo.
    numero = None
    while numero is None:
        try:
            numero = int(input("Escribe un numero: "))
            strnumero = str(numero)
            if numero < 0:
                print(f"Este numero {strnumero} es negativo")
            else:
                print(f"Este numero {strnumero} no es negativo")
        except ValueError:
            print("Solo numneros: ")


def ejercicio03():
    # Hacer un programa en Python que lea un número y determinar si termina en 4.
    numero = None
    while numero is None:
        try:
            numero = int(input("Ingrese el numero a determinar: "))
            if numero % 10 == 4:
                print("Si termina en 4")
            else:
                print("no termina en 4")
        except ValueError:
            print("Solo numeros: ")


def ejercicio04():
    # Hacer un programa en Python que lea tres números enteros y los muestre de menor a mayor.
    numero1 = None
    numero2 = None
    numero3 = None
    while numero1 is None and numero2 is None and numero3 is None:
        try:
            numero1 = int(input("Ingrese el primer numero: "))
            numero2 = int(input("Ingrese el segundo numero: "))
            numero3 = int(input("Ingrese el tercer numero: "))
            strnumero1 = str(numero1)
            strnumero2 = str(numero2)
            strnumero3 = str(numero3)
            if numero1 > numero2:
                if numero2 > numero3:
                    print(
                        f'El orden seria {strnumero3} {strnumero2} {strnumero1}')
                else:
                    if numero1 > numero3:
                        print(
                            f'El orden seria {strnumero2} {strnumero3} {strnumero1}')
                    else:
                        print(
                            f'El orden seria {strnumero2} {strnumero1} {strnumero3}')
            else:
                if numero1 > numero3:
                    print(
                        f'El orden seria {strnumero3} {strnumero1} {strnumero2}')
                else:
                    print(
                        f'El orden seria {strnumero1} {strnumero2} {strnumero3}')
        except ValueError:
            print("Solo numneros: ")


def ejercicio05():
    # Hacer un programa en Python para una tienda de zapatos que tiene una promoción de descuento para vender al mayor, esta dependerá del número de zapatos que se compren. Si son más de diez, se les dará un 10% de descuento sobre el total de la compra; si el número de zapatos es mayor de veinte pero menor de treinta, se le otorga un 20% de descuento; y si son más treinta zapatos se otorgará un 40% de descuento. El precio de cada zapato es de $80.
    numero_zapatos = None
    while numero_zapatos is None:
        try:
            numero_zapatos = int(
                input("Ingrese un numero de zapatos a comprar: "))
            precio_zapato = 80
            if numero_zapatos > 0 and numero_zapatos < 10:
                print("Usted no tiene descuento")
            elif numero_zapatos < 20:
                descuento = 20
            elif numero_zapatos < 30:
                descuento = 30
            elif numero_zapatos >= 30:
                descuento = 40
            else:
                print("solo numeros positivos")
                break
            precio_total = precio_zapato*numero_zapatos
            descuento_total = (precio_total*descuento)/100
            precio_pagar = precio_total - descuento_total
            print(
                f'Vas a comprar {numero_zapatos} y tienes un descuento de {descuento}% y vas a pagar {precio_pagar}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio06():
    # Hacer un programa en Python para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe que si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas entonces las horas extras se le pagarán a $25 por hora.
    horas_trabajadas = None

    while horas_trabajadas is None:
        try:
            horas_trabajadas = int(
                input("Ingrese las horas trabajadas: "))
            if horas_trabajadas > 0 and horas_trabajadas < 40:
                sueldo = horas_trabajadas * 20
            elif horas_trabajadas >= 40:
                horas_extras = horas_trabajadas - 40
                sueldo = 800 + (horas_extras * 25)
            else:
                print("solo numeros positivos")
                break
            print(f'El sueldo es {sueldo}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio07():
    # Hacer un programa en Python para una tienda de helado que da un descuento por compra a sus clientes con membresía dependiendo de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:
    #     Tipo A 10% de descuento
    #    Tipo B 15% de descuento
    #    Tipo C 20% de descuento
    tipo_helado = None

    while tipo_helado is None:
        try:

            precio_helado = int(
                input("el costo del helado es: "))
            if precio_helado > 0:
                tipo_membresia = input(
                    "¿Que tipo de membresia es?(tipo a, b y c): ")
                if tipo_membresia == 'a' or tipo_membresia == 'A':
                    descuento = (precio_helado * 10)/100
                elif tipo_membresia == 'b' or tipo_membresia == 'B':
                    descuento = (precio_helado * 15)/100
                elif tipo_membresia == 'c' or tipo_membresia == 'C':
                    descuento = (precio_helado * 20)/100
                else:
                    print('no es un tipo de membresia valida')
                    break
            else:
                print("solo numeros positivos")
                break
            print(
                f'El precio final de tu helado es {precio_helado - descuento}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio08():
    # Hacer un programa en Python para calcular el promedio de tres notas y determinar si el estudiante aprobó o no.
    nota1 = None
    nota2 = None
    nota3 = None

    while nota1 is None and nota2 is None and nota3 is None:
        try:
            nota1 = int(input("Ingrese la primera nota: "))
            nota2 = int(input("Ingrese la segunda nota: "))
            nota3 = int(input("Ingrese la tercera notas: "))
            if nota1 > 0 and nota2 > 0 and nota3 > 0:
                if nota1 < 21 and nota2 < 21 and nota3 < 21:
                    promedio = (nota1+nota2+nota3)/3
                    print(f'El promedio es {promedio}')
                else:
                    print("las notas deben ser menores a 21")
                break
            else:
                print("solo notas positivos")
                break

        except ValueError:
            print("Solo numeros: ")


def ejercicio09():
    # Hacer un programa en Python para determinar el aumento de un trabajador, se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%, si generaba menos de $2000 su aumento será de un 10%.
    sueldo = None

    while sueldo is None:
        try:
            sueldo = int(
                input("Ingrese el sueldo del trabajador: "))
            if sueldo > 0 and sueldo < 2000:
                incremento = sueldo * 0.1
            elif sueldo >= 2000:
                incremento = sueldo * 0.05
            else:
                print("solo numeros positivos")
                break
            print(f'El incremento es {incremento}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio10():
    # Hacer un programa en Python que diga si un número es par o impar.
    numero = None
    while numero is None:
        try:
            numero = int(
                input("Ingrese el numero: "))
            if numero % 2 == 0:
                print("es un número par")
            else:
                print("es un número impar")
        except ValueError:
            print("Solo numeros: ")


def ejercicio11():
    # Hacer un programa en Python que lea tres números y diga cuál es el mayor.
    numero1 = None
    numero2 = None
    numero3 = None
    while numero1 is None and numero2 is None and numero3 is None:
        try:
            numero1 = int(
                input("Ingrese el primer numero: "))
            numero2 = int(
                input("Ingrese el segundo numero: "))
            numero3 = int(
                input("Ingrese el tercer numero: "))
            if numero1 > numero2 and numero1 > numero3:
                print(f"el mayor es {numero1}")
            elif numero2 > numero1 and numero2 > numero3:
                print(f"el mayor es {numero2}")
            else:
                print(f"el mayor es {numero3}")
        except ValueError:
            print("Solo numeros: ")


def ejercicio12():
    # Hacer un programa en Python que lea dos números y diga cuál es el mayor.
    numero1 = None
    numero2 = None

    while numero1 is None and numero2 is None:
        try:
            numero1 = int(
                input("Ingrese el primer numero: "))
            numero2 = int(
                input("Ingrese el segundo numero: "))
            if numero1 > numero2:
                print(f"el mayor es {numero1}")
            else:
                print(f"el mayor es {numero2}")
        except ValueError:
            print("Solo numeros: ")


def ejercicio13():
    # Hacer un programa en Python que lea una letra y diga si es una vocal.
    letra = None

    while letra is None:
        try:
            letra = input("Ingrese una letra: ")
            if letra == 'A' or letra == 'a':
                print("es una vocal")
            elif letra == 'E' or letra == 'e':
                print("es una vocal")
            elif letra == 'I' or letra == 'i':
                print("es una vocal")
            elif letra == 'O' or letra == 'o':
                print("es una vocal")
            elif letra == 'U' or letra == 'u':
                print("es una vocal")
            else:
                print("no es una vocal")
        except ValueError:
            print("Solo letras: ")


def ejercicio14():
    # Hacer un programa en Python que lea un entero positivo del 1 al diez y al 9 y determine si es un número primo.
    numero = None

    while numero is None:
        try:
            numero = int(input("Ingrese una numero: "))
            if numero <= 10 and numero > 0:
                if numero == 2:
                    print("es un número primo")
                elif numero == 3:
                    print("es un número primo")
                elif numero == 5:
                    print("es un número primo")
                elif numero == 7:
                    print("es un número primo")
                else:
                    print("no es un número primo")
            else:
                print("el numero debe ser mayor a 0 y menor a 11")
        except ValueError:
            print("Solo letras: ")


def ejercicio15():
    # Hacer un programa en Python que convierta centímetros a pulgadas y libras a kilogramos.
    opcion_elegida = None
    while opcion_elegida is None:
        try:
            opcion_elegida = int(
                input("digite 1 para centimetros a pulgadas o 2 para libras a kilogramos: "))
            if opcion_elegida == 1:
                distancia = int(
                    input("Ingrese el valor de la distancia en centimetros: "))
                pulgadas = distancia / 2.54
                print(f"Las pulgadas son {pulgadas}")
            elif opcion_elegida == 2:
                peso = int(input("Ingrese el valor del peso en libras: "))
                kilos = peso / (1 / 2.21)
                print(f'Los kilogramos son {kilos}')
            else:
                print("opcion incorrecta")
        except ValueError:
            print("Solo numeros: ")


def ejercicio16():
    # Hacer un programa en Python que lea un número y según ese número, indique el día que corresponde.
    numero_dia = None
    while numero_dia is None:
        try:
            numero_dia = int(input("Introduce el numero de dia: "))
            if numero_dia == 1:
                print(f'El numero {numero_dia} corresponde al dia lunes')
            elif numero_dia == 2:
                print(f'El numero {numero_dia} corresponde al dia martes')
            elif numero_dia == 3:
                print(f'El numero {numero_dia} corresponde al dia miercoles')
            elif numero_dia == 4:
                print(f'El numero {numero_dia} corresponde al dia jueves')
            elif numero_dia == 5:
                print(f'El numero {numero_dia} corresponde al dia viernes')
            elif numero_dia == 6:
                print(f'El numero {numero_dia} corresponde al dia sabado')
            elif numero_dia == 7:
                print(f'El numero {numero_dia} corresponde al dia domingo')
            else:
                print("opcion incorrecta")
        except ValueError:
            print("Solo numeros: ")


def ejercicio17():
    # Hacer un programa en Python donde se ingrese una hora y nos calcule la hora dentro de un segundo.
    hora = None
    minutos = None
    segundos = None
    while hora is None and minutos is None and segundos is None:
        try:
            hora = int(input("Ingrese la hora: "))
            minutos = int(input("Ingrese los minutos: "))
            segundos = int(input("Ingrese los segundos: "))
            if (hora < 24 and minutos < 59 and segundos < 59) and (hora >= 0 and minutos >= 0 and segundos >= 0):
                segundos = segundos + 1
            elif hora == 23 and minutos == 59 and segundos == 59:
                hora = 0
                segundos = 00
                minutos = 00
            elif minutos == 59 and segundos == 59:
                hora = hora + 1
                segundos = 00
                minutos = 00
            elif segundos == 59:
                minutos = minutos + 1
                segundos = 00

            else:
                print(
                    'la hora máxima es 23, los segundos máximos son 59 y los segundos máximos son 59 o colocaste negativos')
                break
            strhora = str(hora)
            strminutos = str(minutos)
            strsegundos = str(segundos)
            print(f'la nueva hora es  {strhora}:{strminutos}:{strsegundos}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio18():
    # Hacer un programa en Python para una empresa se encarga de la venta y distribución de CD vírgenes. Los clientes pueden adquirir los artículos (supongamos un único producto de una única marca) por cantidad. Los precios son:
    # $10. Si se compran unidades separadas hasta 9.
    # $8. Si se compran entre 10 unidades hasta 99.
    # $7. Entre 100 y 499 unidades.
    # $6. Para mas de 500 unidades.
    # La ganancia para el vendedor es de 8,25 % de la venta. Realizar un algoritmo en Pseint que dado un número de CDs a vender calcule el precio total para el cliente y la ganancia para el vendedor.
    cantidad_cds = None
    total = None
    while cantidad_cds is None and total is None:
        try:
            cantidad_cds = int(input("Ingrese la cantidad de cds vendidos: "))
            if cantidad_cds > 499:
                total = cantidad_cds * 6
            elif cantidad_cds <= 499 and cantidad_cds >= 100:
                total = cantidad_cds * 7
            elif cantidad_cds < 100 and cantidad_cds >= 10:
                total = cantidad_cds * 8
            elif cantidad_cds <= 9 and cantidad_cds > 0:
                total = cantidad_cds * 10
            else:
                print('la cantidad no puede ser negativa')
                break
            print(f'Vas a pagar {total}')
            print(f'La ganancia del vendedor es {total * 0.0825}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio19():
    # Hacer un programa en Python para una heladería se tienen 4 tipos de empleados ordenados de la siguiente forma con su número identificador y salario diario correspondiente:
    # Cajero (56$/día).
    # Servidor (64$/día).
    # Preparador de mezclas (80$/día).
    # Mantenimiento (48$/día).
    # El dueño de la tienda desea tener un programa donde sólo ingrese dos números enteros que representen al número identificador del empleado y la cantidad de días que trabajó en la semana (6 días máximos). Y el programa le mostrará por pantalla la cantidad de dinero que el dueño le debe pagar al empleado que ingresó
    dias_trabajados = None
    tipo_empleado = None
    while dias_trabajados is None and tipo_empleado is None:
        try:
            tipo_empleado = input(
                "Ingresar el identificador del empleado: (cajero:01, Servidor:02, Preparador de mezclas:03, Mantenimiento:04): ")
            dias_trabajados = int(input("¿Cuántos días tranajó: "))
            if dias_trabajados < 7:
                if tipo_empleado == '01':
                    salario = dias_trabajados * 56
                elif tipo_empleado == '02':
                    salario = dias_trabajados * 64
                elif tipo_empleado == '03':
                    salario = dias_trabajados * 80
                elif tipo_empleado == '04':
                    salario = dias_trabajados * 48
                else:
                    print('No es un identificador de empleado')
                    break
            else:
                print('La mínima cantida de dias es 1 y máxima es 6')
                break
            print(f'El salario del empleado es {salario}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio20():
    # Hacer un programa en Python que que lea 4 números enteros positivos y verifique y realice las siguientes operaciones:
    # ¿Cuántos números son Pares?
    # ¿Cuál es el mayor de todos?
    # Si el tercero es par, calcular el cuadrado del segundo.
    # Si el primero es menor que el cuarto, calcular la media de los 4 números.
    # Si el segundo es mayor que el tercero, verificar si el tercero esta comprendido entre los valores 50 y 700. Si cumple se cumple la segunda condición, calcular la suma de los 4 números.
    numero1 = None
    numero2 = None
    numero3 = None
    numero4 = None

    while numero1 is None and numero2 is None and numero3 is None and numero4 is None:
        try:
            numero1 = int(
                input("Ingrese el primer numero: "))
            numero2 = int(
                input("Ingrese el segundo numero: "))
            numero3 = int(
                input("Ingrese el tercer numero: "))
            numero4 = int(
                input("Ingrese el cuarto numero: "))
            regla_01 = False
            contador_pares = 0
            regla_02 = True
            numero_mayor = 0
            regla_03 = False
            cuadrado_segundo = 0
            regla_04 = False
            media = 0
            regla_05 = False
            suma_numeros = 0
            if numero1 % 2 == 0:
                contador_pares = contador_pares+1
            if numero1 > numero_mayor:
                numero_mayor = numero1

            if numero2 % 2 == 0:
                contador_pares = contador_pares+1
            if numero2 > numero_mayor:
                numero_mayor = numero2

            if numero3 % 2 == 0:
                regla_03 = True
                contador_pares = contador_pares+1
                cuadrado_segundo = numero2**2
            if numero3 > numero_mayor:
                numero_mayor = numero3

            if numero4 % 2 == 0:
                contador_pares = contador_pares+1
            if numero4 > numero_mayor:
                numero_mayor = numero4
            if numero1 < numero4:
                regla_04 = True
                media = (numero1+numero2+numero3+numero4)/4
            if numero2 > numero3:
                if numero3 > 50 and numero3 < 700:
                    regla_05 = True
                    suma_numeros = (numero1+numero2+numero3+numero4)
            if contador_pares != 0:
                regla_01 = True
            if regla_01 == True:
                print("La cantidad de numeros pares encontrados es : ",
                      contador_pares)
            if regla_02 == True:
                print("El numero mayor es : ", numero_mayor)
            if regla_03 == True:
                print("El cuadrado del segundo numero es : ", cuadrado_segundo)
            if regla_04 == True:
                print("La media aritmetica de los 4 numeros es: ", media)
            if regla_05 == True:
                print("La suma de los 4 numeros es: ", suma_numeros)
        except ValueError:
            print("Solo numeros: ")


def ejercicio21():
    # Hacer un programa en Python que permita calcular el factorial de un número.
    numero = None
    while numero is None:
        try:
            numero = int(input("Brindame un numero y te doy el factorial: "))
            factorial = 1
            for i in range(1, numero+1):
                factorial = factorial*i
            print(
                f'El factorial es {factorial}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio22():
    # Hacer un programa en Python para calcular la suma de los n primeros números.
    numero = None
    while numero is None:
        try:
            numero = int(input("Brindame un numero: "))
            sumatoria = 0
            for i in range(1, numero+1):
                sumatoria = sumatoria+i
            print(
                f'La sumatoria de los {numero} primeros numeros es {sumatoria}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio23():
    # Hacer un programa en Python para calcular la suma de los números impares menores o iguales a n.
    numero = None
    while numero is None:
        try:
            numero = int(input("Brindame un numero: "))
            sumatoria = 0
            for i in range(1, numero+1):
                if i % 2 == 1:
                    sumatoria = sumatoria+i
            print(
                f'La sumatoria es {sumatoria}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio24():
    # Hacer un programa en Python para realizar la suma de todos los números pares hasta el 1000.
    sumatoria = 0
    for i in range(1, 1001):
        if i % 2 == 0:
            sumatoria = sumatoria+i
    print(
        f'La sumatoria es {sumatoria}')


def ejercicio25():
    # Hacer un programa en Python para calcular el factorial de un número de una forma distinta.
    numero = None
    while numero is None:
        try:
            numero = int(input("Brindame un numero y te doy el factorial: "))
            factorial = 1
            if numero < 0:
                print('el número {numero} no se puede calcular')
            else:
                for i in range(1, numero+1):
                    factorial = factorial*i
                print(
                    f'El factorial es {factorial}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio26():
    # Hacer un programa en Python para calcular el resto y cociente por medio de restas sucesivas.
    dividendo = None
    divisor = None
    while dividendo is None and divisor is None:
        try:
            dividendo = int(input("Ingrese el dividendo: "))
            divisor = int(input("Ingrese el divisor: "))
            if dividendo > divisor:
                resto = dividendo % divisor
                cociente = (dividendo - resto) // divisor
            else:
                print('la division seria impropia')
                break
            print(f'El cociente es {cociente}')
            print(f'La resto es {resto}')
        except ValueError:
            print("Solo numeros: ")


def ejercicio27():
    # Hacer un programa en Python para calcular el resto y cociente por medio de restas sucesivas.
    numero = None
    while numero is None:
        try:
            suma = 0
            cantidad_numeros = 0
            while True:
                numero = int(input("Ingrese el numero: "))
                if numero >= 0:
                    suma = suma + numero
                    cantidad_numeros = cantidad_numeros + 1
                else:
                    print('no puedes colocar negativos')
                    break
                print("La media es ", suma/cantidad_numeros)
        except ValueError:
            print("Solo numeros: ")


def ejercicio28():
    # Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo repetir.
    sumatoria = 0
    for i in range(1, 101):
        sumatoria = sumatoria+i
    print(
        f'La sumatoria es {sumatoria}')


def ejercicio29():
    # Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo repetir.
    cantidad_numeros = 0
    numeros= 1
    suma = 0
    while True:
        if numeros >= 1 and numeros < 101:
            suma = suma + numeros
            numeros = numeros + 1
        else:
            print(f"La suma es {suma}")
            break


def ejercicio30():
    # Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo repetir.
    sumatoria = 0
    for i in range(1, 101):
        sumatoria = sumatoria+i
    print(
        f'La sumatoria es {sumatoria}')


def ejercicio31():
    # Hacer un programa en Python parar calcular la media de los números pares e impares, sólo se ingresará diez números.
    numero = None
    while numero is None:
        try:
            suma_pares = 0
            suma_impares = 0
            numero = int(input("Ingrese el numero: "))
            for numero in range(numero, numero+10):
                if numero % 2 == 0:
                    suma_pares = suma_pares + numero
                    promedio_pares = suma_pares / 5
                else:
                    suma_impares = suma_impares + numero
                    promedio_impares = suma_impares / 5
            print(f"La media de los pares es {promedio_pares}")
            print(f"La media de los impares es {promedio_impares}")
        except ValueError:
            print("Solo numeros: ")


def ejercicio33():
    # Hacer un programa en Python que permita al usuario continuar con el programa
    respuesta = None
    while respuesta is None :
        try:
            while True:
                respuesta = input("Ingrese s para que continue y n para terminar: ")
                if respuesta == 's':
                    print('se continua ejevutando')
                else:
                    print('el progrma se va a cerrar')
                    break
        except ValueError:
            print("Solo numeros: ")