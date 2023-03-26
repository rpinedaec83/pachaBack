def ejercicio01():
    #Hacer un programa en Python que lea un numero por el teclado y determine si tiene 3 digitos
    numero = int(input("Escribe un numero: "))
    strnumero = str(numero)
    if len(strnumero) == 3:
        print(f"Este numero tiene {len(strnumero)} digitos")
    else:
        print(f"Este numero no cumple con la condicion solo tiene {len(strnumero)} digitos")

def ejercicio02():
    #Hacer un programa en Python que lea un numero entero por el teclado y determinar si es negativo
    numero = int(input("Ingrese un numero: "))
    if numero>=0:
        print("El mumero es positivo")
    else:
        print("El numero es negativo")

def ejercicio03():
    #acer un algoritmo en Pseint que lea un número y determinar si termina en 4.
    numero = None #vacio

    while numero is None:#vacio, correcto, incorrecto
        try:#va a intentar si sale mal va al except
            numero = int(input("Ingrese el numero a determinar: "))
            if numero % 10 == 4:
                print("Termina en 4")
            else:
                print("No termina en 4")
        except ValueError:
            print("Solo numeros: ")

def ejercicio04():
    #Hacer un algoritmo en Pseint que lea tres números enteros y los muestre de menor a mayor.
        num1 = int()
        num2 = int()
        num3 = int()
        print("Ingrese el primer numero")
        num1 = int(input())
        print("Ingrese el segundo numero")
        num2 = int(input())
        print("Ingrese el tercer numero")
        num3 = int(input())
        if num1<=num2 and num1<=num3:
            print(num1)
            if num2<=num3:
                print(num2)
                print(num3)
            else:
                print(num3)
                print(num2)
        else:
            if num2<=num1 and num2<=num3:
                print(num2)
                if num1<=num3:
                    print(num1)
                    print(num3)
                else:
                    print(num3)
                    print(num1)
            else:
                print(num3)
                if num1<=num2:
                    print(num1)
                    print(num2)
                else:
                    print(num2)
                    print(num1)

def ejercicio05():
        cantidaddezapatos = int()
        descuento = int()
        precio = float()
        preciototal = float()
        print("Ingrese la cantidad de zapatos a comprar ")
        cantidaddezapatos = int(input())
        precio = 80
        preciototal = cantidaddezapatos*precio
        if cantidaddezapatos>30:
            descuento = 40
        else:
            if cantidaddezapatos>20:
                descuento = 20
            else:
                if cantidaddezapatos>10:
                    descuento = 10
                else:
                    descuento = 0
        preciototal = preciototal-(preciototal*descuento/100)
        print("El precio total es: $",preciototal)

def ejercicio06():
    #Hacer un programa en Python para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe que si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas entonces las horas extras se le pagarán a $25 por hora.
        horas_trabajadas = int()
        sueldo_semanal = int()
        sueldo_base = 20
        sueldo_extra = 25
        print("Ingrese horas trabajadas en la semana ")
        horas_trabajadas = int(input())
        if horas_trabajadas>40:
            sueldo_semanal = horas_trabajadas*sueldo_extra
        else:
            sueldo_semanal = horas_trabajadas*sueldo_base
        print("El total que gana el trabajador por semana es: ",sueldo_semanal)

def ejercicio07():
        a = str()
        b = str()
        c = str()
        x = str()
        descuento = str()
        print("Ingrese que tipo de membresia tiene: ")
        x = input()
        if x==a:
            descuento = "10%"
        else:
            if x==b:
                descuento = "15%"
            else:
                descuento = "20%"
        print("El descuento por la membresia : ",x," es: ",descuento)

def ejercicio08():
        nota1 = float()
        nota2 = float()
        nota3 = float()
        promedio = float()
        print("********Promedio de notas********** ")
        print("Ingrese la nota 1: ")
        nota1 = float(input())
        print("Ingrese la nota 2: ")
        nota2 = float(input())
        print("Ingrese la nota 3: ")
        nota3 = float(input())
        promedio = (nota1+nota2+nota3)/3
        if promedio>=10.5:
            print("El estudiante aprobo ")
        else:
            print("El estudiante desaprobo ")

def ejercicio09():
        sueldo = float()
        aumento = float()
        print("Ingrese el sueldo del trabajador: ")
        sueldo = float(input())
        if sueldo>2000:
            aumento = sueldo*0.05
        else:
            aumento = sueldo*0.1
        print("El aumento correspondiente es de $ :",aumento)
    
def ejercicio10():
        num = int()
        print("Ingrese numero: ")
        num = int(input())
        if num%2==0:
            print("El numero es par")
        else:
            print("El numero es impar")

def ejercicio11():
        num1 = int()
        num2 = int()
        num3 = int()
        mayior = int()
        print("Ingrese el primer numero: ")
        num1 = int(input())
        print("Ingrese el segundo numero: ")
        num2 = int(input())
        print("Ingrese el tercer numero: ")
        num3 = int(input())
        if num1>=num2 and num1>=num3:
            mayior = num1
        else:
            if num2>=num1 and num2>=3:
                mayior = num2
            else:
                mayior = num3
        print("El mayor de los tres numeros es: ",mayior)

def ejercicio12():
        num1 = int()
        num2 = int()
        mayior = int()
        print("Ingrese el primer numero ")
        num1 = int(input())
        print("Ingrese el segundo numero ")
        num2 = int(input())
        if num1>=num2:
            mayior = num1
        else:
            mayior = num2
        print("El numero mayor es: ",mayior)

def ejercicio13():
        letra = str()
        print("Ingrese una letra: ")
        letra = input()
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
            print("La letra es una vocal ")
        else:
            print("La letra no es una vocal.")

def ejercicio14():
        numero = int()
        primo = bool()
        print("Ingrese numero: ")
        numero = int(input())
        if numero<1 or numero>10:
            print("El numero ingresado no es valido")
        else:
            primo = True
            for i in range(2,numero):
                if numero%1==0:
                    primo = False
            if primo:
                print("El numero es primo")
            else:
                print("El numero no es primo")
    


def ejercicio15():
    #Hacer un algoritmo en Pseint que convierta centímetros a pulgadas y libras a kilogramos..
    
        centimetros = float()
        pulgadas = float()
        libras = float()
        kilogramos = float()
        print("Ingrese la cantidad de centimetros a convertir ")
        centimetros = float(input())
        pulgadas = centimetros/2.54
        print("El resultado de la conversion es: ",pulgadas," pulgadas")
        print("Ingrese la cantidad de libras a convertir: ")
        libras = float(input())
        kilogramos = libras*0.453592
        print("El resultado de la conversion es: ",kilogramos," kilogramos")
     



def ejercicio16():
    #Hacer un algoritmo en Pseint que lea un número y según ese número, indique el día que corresponde.
    numero = None
    while numero is None:
        try:
            numero = int(input("Ingrese numero : "))
            if numero == 1:
                print("Lunes")
            elif numero ==2:
                print("Martes")
            elif numero ==3:
                print("Miercoless")
            elif numero ==4:
                print("Jueves")
            elif numero ==5:
                print("Viernes")
            elif numero ==6:
                print("Sabado")
            else:
                print("Domingo")
        except ValueError:
            print("Solo numeros: ")




def ejercicio17():
    #Hacer un algoritmo en Pseint donde se ingrese una hora y nos calcule la hora dentro de un segundo.
        hora = int()
        minuto = int()
        segundoo = int()
        print("Ingrese la hora en formato de 24 horas ")
        hora = int(input())
        print("Ingrese el minuto ")
        minuto = int(input())
        print("Ingrese el segundo ")
        segundoo = int(input())
        segundoo = segundoo+1
        if segundoo==60:
            segundoo = 0
            minuto = minuto+1
            if minuto==60:
                minuto = 0
                hora = hora+1
                if hora==24:
                    hora = 0
        print("La hora dentro de un segundo es: ",hora,":",minuto,":",segundoo)




def ejercicio18():
#Hacer un algoritmo en Pseint para una empresa se encarga de la venta y distribución de CD vírgenes. Los clientes pueden adquirir los artículos (supongamos un único producto de una única marca) por cantidad. Los precios son:
#$10. Si se compran unidades separadas hasta 9.
#$8. Si se compran entre 10 unidades hasta 99.
#$7. Entre 100 y 499 unidades.
#$6. Para mas de 500 unidades.
#La ganancia para el vendedor es de 8,25 % de la venta. Realizar un algoritmo en Pseint que dado un número de CDs a vender calcule el precio total para el cliente y la ganancia para el vendedor.
        ventas = int()
        total = int()
        total = 0
        print("Cuantos CDS vendio?")
        ventas = int(input())
        if (ventas<=9):
            total = ventas*10
        else:
            if (ventas<=99):
                total = ventas*8
            else:
                if (ventas<=499):
                    total = ventas*7
                else:
                    if (ventas>499):
                        total = ventas*6
        print("Total a pagar por el cliente :",total)
        print("Ganancias del vendedor: ",total*0.0825)

def ejercicio19():
        print("Ingrese los numeros que representan al empreado ")
        tipo = float(input())
        print("Ingrese el numero de dias trabajados")
        diastrabajados = input()
        if diastrabajados<=6:
            if tipo==1:
                print("El monto total a pagar a un cajedo es de: ",(diastrabajados*56))
            elif tipo==2:
                print("El monto total a pagar a un cajedo es de: ",(diastrabajados*64))
            elif tipo==3:
                print("El monto total a pagar a un cajedo es de: ",(diastrabajados*80))
            elif tipo==4:
                print("El monto total a pagar a un cajedo es de: ",(diastrabajados*48))
        else:
            print("El numero de dias exede a 6 ",diastrabajados)

def ejercicio20():
        num1 = int()
        num2 = int()
        num3 = int()
        num4 = int()
        suma = int()
        print("Ingrese el primer numero")
        num1 = int(input())
        print("Ingrese el segundo numero")
        num2 = int(input())
        print("Ingrese el tercer numero")
        num3 = int(input())
        print("Ingrese el cuarto numero")
        num4 = int(input())
        if num2>num3:
            if num3>=50 and num3<=700:
                suma = num1+num2+num3+num4
                print("La suma de los cuatro numeros es ",suma)
            else:
                print("El tercer numero no cumple la segunda condicion")


def ejercicio21():
    #Hacer un algoritmo en Pseint que permita calcular el factorial de un número.
        numeroo = int()
        factorial = int()
        print("Ingrese numero a calcular el factorial ")
        numeroo = int(input())
        factorial = 1
        for i in range(1,numeroo+1):
            factorial = factorial*i
        print("El factorial es ",factorial)

def ejercicio22():
    #acer un algoritmo en Pseint para calcular la suma de los n primeros números.
    numero = None
    while numero is None:
        try:
            numero = int(input("Ingrese numero a calcular el factorial: "))
            factorial=1
            for i in range(1,numero+1):
                factorial *= i
            print(f"El factorial es {factorial}")
        except ValueError:
            print("Solo numeros: ")

def ejercicio23():
        #Hacer un programa en Python para calcular la suma de los números impares menores o iguales a n.
        print("Ingrese un numero entero positivo: ")
        numeroenteroingresado = float(input())
        count = 0
        for i in range(1,numeroenteroingresado+1,2):
            count = count+i
        print("La suma de los numeros ",count)

def ejercicio24():
        #Hacer un programa en Python para realizar la suma de todos los números pares hasta el 1000.
        count = 0
        i = 0
        while i<=1000:
            if i%2==0:
                count = count+i
            i = i+1
        print("La suma de los 1000 numeros pares es: ",count)
     
def ejercicio25():
        #Hacer un programa en Python para calcular el factorial de un número de una forma distinta.
        numero = int()
        factorial = int()
        print("Brindame un numero y te doy el factorial")
        numero = int(input())
        if numero<0:
            print("El numero ",numero,"no se puede calcular")
        else:
            x = 1
            factorial = 1
            while True:# no hay 'repetir' en python
                factorial = factorial*x
                x = x+1
                if x>numero: break
            print(factorial)

     
def ejercicio26():
        #Hacer un programa en Python para calcular el resto y cociente por medio de restas sucesivas.
        print("Primer numero")
        a = float(input())
        print("Segundo numero")
        b = float(input())
        cociente = 0
        while a>=b:
            a = a-b
            cociente = cociente+1
        print("El Cociente es: ",cociente)
        print("El resto es: ",a)
     
def ejercicio27():
        #Hacer un programa en Python para determinar la media de una lista indefinida de números positivos, se debe acabar el programa al ingresar un número negativo.
        c = int()
        x = float()
        suma = float()
        x = 1
        suma = 0
        c = 0
        while x>=0:
            print("Ingresa cualquier numero positivo ")
            x = float(input())
            if x>=0:
                suma = suma+x
                c = c+1
        if c>0:
            print("La media es ",suma/c)
def ejercicio28():
        #Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo repetir.
        count = 1
        suma = 0
        while True:# no hay 'repetir' en python
            suma = suma+count
            count = count+1
            # por posicion array
            if count==101: break
        print("ciclo repetir: La suma de 1 a 100 es: ",suma)
     
def ejercicio29():
        #Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo mientras.
        contador = int()
        suma = int()
        contador = 1
        suma = 0
        while contador<=100:
            suma = suma+contador
            contador = contador+1
        print(" La suma de los 100 numeros es ",suma)
     


def ejercicio30():
    #Hacer un algoritmo en Pseint para calcular la suma de los primeros cien números con un ciclo para.
    suma = None
    while suma is None:
        try:
            suma=0
            for i in range(1,101):
                suma += i
            print(f"La suma de los priemros cien numeros es: {suma}")
        except ValueError:
            print("Error")


def ejercicio31():
#Hacer un algoritmo en Pseint parar calcular la media de los números pares e impares, sólo se ingresará diez números.
    while True:
        try:
            par=0
            impar=0
            sumap=0
            sumai=0
            for i in range(10):
                num=int(input("Ingrese numero: "))
                if num % 2 == 0:
                    sumap += num
                    par += 1
                else:
                    sumai += num
                    impar += 1
            mediap=sumap/par
            mediai=sumai/impar

            print(f"La media de los pares es: {mediap}")
            print(f"La media de los impares es: {mediai}")
        except ValueError:
            print("Debes ingresar un numero, Intenta nuevamente...")

def ejercicio32():
#Se quiere saber cuál es la ciudad con la población de más personas, son tres provincias y once ciudades, Hacer un programa en Python que nos permita saber eso. Datos de Lambayeque, Lima, Loreto
    provincias = {
        'Lambayeque': {'Chiclayo': 730000, 'Ferreniafe':63000},
        'Lima': {'Lima': 8852000, 'Callao': 1000000, 'San Juan de Lurigancho': 1013000, 'San Martín de Porres': 648000, 'Surco': 331000},
        'Loreto': {'Iquitos': 447000, 'Yurimaguas': 50200, 'Nauta': 14300}
    }
    #Encontrando la ciudad mas grande
    cuidad_mas_grande = None
    poblacion_mas_grande = 0

    for provincia,cuidades in provincias.items():
        for cuidad, poblacion in cuidades.items():
            if poblacion > poblacion_mas_grande:
                cuidad_mas_grande = cuidad
                poblacion_mas_grande = poblacion

    print(f"La cuidad con la poblacion mas grande es {cuidad_mas_grande} con una poblacion de {poblacion_mas_grande} personas.")
        
def ejercicio33():
    #Hacer un programa en Python que permita al usuario continuar con el programa.
    respuesta = input("Presiona Enter para continuar o escribe 'salir' para salir: ")

    if respuesta.lower()=="salir":
        print("Adios!")
    else:
        print("Continuando con el programa...")


def ejercicio34():
    #Hacer un programa en Python que imprima la tabla de multiplicar de los números del uno nueve.
    for i in range(1,10):
        for j in range(1,11):
            print(i,"x","=",i*j)
        print()

def ejercicio35():
    #Hacer un programa en Python que nos permita saber cuál es el número mayor y menor, se debe ingresar sólo veinte números.
    while True:
        try:
            menor=999
            mayor=0
            for i in range(20):
                numero = int(input("Ingrese un numero: "))
                if numero>mayor:
                    mayor=numero
                elif numero<menor:
                    menor=numero
            print(f"El numero mayor es: {mayor} ")
            print(f"El numero menor es: {menor} ")
            break
        except ValueError:
            print("Debes ingresar un numero. Intenta nuevamente...")

def ejercicio36():
    #Hacer un programa en Python para calcular la serie de Fibonacci.
    n=int(input("Introduice un numero: "))

    a,b =0 ,1
    print(a)
    print(b)

    for i in range(2,n):
        c=a+b
        a,b=b,c
        print(c)

def ejercicio37():
    #Hacer un programa en Python para conseguir el M.C.D de un número por medio del algoritmo de Euclides.
    a=int(input("Ingrese el primer numero: "))
    b=int(input("Ingrese el segundo numero: "))
    while b != 0:
        r=a % b
        a=b
        b=r
    print(F"El MCD de los dos numeros es: {a}")

def ejercicio38():
    #Hacer un programa en Python que nos permita saber si un número es un número perfecto.

        numero = int()
        suma_divisores = int()
        print("Ingrese numero: ")
        numero = int(input())
        suma_divisores = 0
        for i in range(1,numero):
            if numero%i==0:
                suma_divisores = suma_divisores+i
        if suma_divisores==numero:
            print(numero," es un numero perfecto. ")
        else:
            print(numero," no es un numero perfecto. ")

def ejercicio39():
    #Hacer un programa en Python que cumpla con la aproximación del número pi con la serie de Gregory-Leibniz. La formula que se debe aplicar es:
    # Pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...

	pii = float()
	denominador = float()
	print("Ingrese la cantidad de terminoa a utilizar ")
	n = int(input())
	pii = 0
	denominador = 1
	for i in range(1,n+1):
		pii = pii+(4/denominador)
		denominador = denominador+2
		pii = pii-4/denominador
		denominador = denominador+2
	print("La aproximacion de Pi con ",n," Terminos es: ",pii)
   
def ejercicio40():
    #Hacer un programa en Python que cumpla con la aproximación del número pi con la serie de Nilakantha. La formula que se debe aplicar es:
    #Pi = = 3 + 4/(234) - 4/(456) + 4/(678) - 4/(8910) + 4/(101112) - 4/(121314) ...
      
        print("Ingrese la cantidad de terminos para la aproximacion de Pii: ")
        n= int(input())
        pii=3.0
        for i in range(n):
            denominador = (2*i+2)*(2*i+3)*(2*i+4)
            if i%2==0:
                pii = pii+4/denominador
            else:
                pii = pii-4/denominador
        print("El valor aproximado de PI con ",n,"terminos es: ",pii)
