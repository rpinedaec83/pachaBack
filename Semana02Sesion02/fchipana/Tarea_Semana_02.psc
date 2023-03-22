//1.	Hacer un algoritmo en Pseint que lea un número por el teclado y determinar si tiene tres dígitos.
Proceso Tarea_Semana_02
	numero_tarea = 50
	
	Mientras  numero_tarea <> 100
		
	Escribir ""
	Escribir  "* MENU DE TAREAS * "
	Escribir "Ingrese la tarea a reproducir:"
	Leer numero_tarea
		
	Segun numero_tarea Hacer
		1:	
			tarea_01()
		2:	
			tarea_02()
		3:	
			tarea_03()
		4:	
			tarea_04()
		5:	
			tarea_05()
		6:	
			tarea_06()
		7:	
			tarea_07()
		8:	
			tarea_08()
		9:	
			tarea_09()
		10:	
			tarea_10()
		11:	
			tarea_11()
		12:	
			tarea_12()
		13:	
			tarea_13()
		14:	
			tarea_14()
		15:	
			tarea_15()
		16:	
			tarea_16()
		17:	
			tarea_17()
		18:	
			tarea_18()
		19:	
			tarea_19()
		20:	
			tarea_20()
		21:	
			tarea_21()
		22:	
			tarea_22()
		23:	
			tarea_23()
		24:	
			tarea_24()
		25:	
			tarea_25()
		26:	
			tarea_26()
		27:	
			tarea_27()
		28:	
			tarea_28()
		29:	
			tarea_29()
		30:	
			tarea_30()
		31:	
			tarea_31()
		32:	
			tarea_32()
		33:	
			tarea_33()
		34:	
			tarea_34()
		35:	
			tarea_35()
		36:	
			tarea_36()
		37:	
			tarea_37()
		38:	
			tarea_38()
		39:	
			tarea_39()
		40:	
			tarea_40()
			
		De Otro Modo:
			Escribir "La tarea indicada no existe."
	Fin Segun
FinMientras

FinProceso

//TAREAS
Funcion tarea_01()	
	Escribir "1.    Hacer un algoritmo en Pseint que lea un número entero por el teclado y determinar si es negativo."
	Definir input Como Entero
	
	Escribir ""
	Escribir  "Ingrese un numero para validar si tiene 3 digitos: "
	Leer input
	input_fijo = input
	contador_cociente_menor_igual_1 = 0
	Mientras input >= 1 Hacer
		input = trunc(input/10)
		contador_cociente_menor_igual_1 = contador_cociente_menor_igual_1 +1
	FinMientras
	
	Escribir "El numero ", input_fijo, "  ", contador_cociente_menor_igual_1, " digitos."
	
FinFuncion	

Funcion tarea_02()	
	Definir input Como Entero
	Escribir "2.    Hacer un algoritmo en Pseint que lea un número entero por el teclado y determinar si es negativo."
	Escribir ""
	Escribir  "Ingrese un numero para validar si es negativo: "
	Leer input
	
	si input < 0 Entonces
		Escribir  "El numero ", input, " es negativo"
	SiNo
		Escribir  "El numero ", input, " no es negativo"
	FinSi
		
FinFuncion	

Funcion tarea_03()	
	Escribir "3.    Hacer un algoritmo en Pseint que lea un número y determinar si termina en 4."
	Definir input Como Entero
	
	Escribir ""
	Escribir  "Ingrese un numero para validar si termina en 4: "
	Leer input
	
	U = input MOD 10
	
	si U = 4 Entonces
		Escribir  "El numero ", input, " si termina en 4."
	SiNo
		Escribir  "El numero ", input, " no termina en 4."
	FinSi
	
FinFuncion	

Funcion tarea_04()	
	Escribir "4.    Hacer un algoritmo en Pseint que lea tres números enteros y los muestre de menor a mayor."
	Definir n1, n2, n3 Como Entero;
	Escribir 'Ingrese tres números:';
	Leer n1;
	Leer n2;
	Leer n3;
	
	si (n1 < n2 y n1 < n3) entonces
		si (n2 < n3)
			Escribir n1," ", n2, " ", n3;
		SiNo
			Escribir n1," ", n3, " ",n2;
		FinSi
	FinSi
	
	si (n2 < n1 y n2 < n3) Entonces
		si (n1 < n3) Entonces
			Escribir n2," ", n1," ", n3;
		SiNo
			Escribir n2," ", n3," ", n1;
		FinSi
	FinSi
	
	si (n3 < n1 y n3 < n2) Entonces
		si (n1 < n2)
			Escribir n3," ", n1," ", n2;
		SiNo
			Escribir n3," ", n2," ", n1;
		FinSi
	FinSi
		
FinFuncion	


Funcion tarea_05()	
	Escribir "5.    Hacer un algoritmo en Pseint para una tienda de zapatos que tiene una promoción de descuento para vender al mayor, esta dependerá del número de zapatos que se compren. Si son más de diez, se les dará un 10% de descuento sobre el total de la compra; si el número de zapatos es mayor de veinte pero menor de treinta, se le otorga un 20% de descuento; y si son más treinta zapatos se otorgará un 40% de descuento. El precio de cada zapato es de $80."
	Definir nroZapatos,precio Como Entero;
	precio <- 0;
	
	Escribir "Cantidad de Zapatos a comprar:";
	Leer nroZapatos;
	precio <- nroZapatos * 80;
	
	si (nroZapatos < 10) entonces
		Escribir "No se aplica descuento. El precio total a pagar es: ", precio;
	SiNo
		si(nroZapatos < 20) entonces
			Escribir "Se aplica descuento. El precio total a pagar es: ", precio - (precio * 0.1);
		sino 
			si(nroZapatos < 30) Entonces
				Escribir " Se aplica descuento. El precio total a pagar es: ", precio - (precio * 0.2);
			SiNo
				Escribir "Se aplica descuento. El precio total a pagar es: ", precio - (precio * 0.4);
			FinSi
		FinSi
	FinSi
FinFuncion	

Funcion tarea_06()	
	Escribir "6.    Hacer un algoritmo en Pseint para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe que si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas entonces las horas extras se le pagarán a $25 por hora."
	Definir horasTrab, sueldo, horasExtra Como Entero;
	horasExtra <- 0;
	sueldo <- 0;
	
	Escribir "Ingresar horas trabajadas:";
	Leer horasTrab;
	
	si (horasTrab < 40) entonces
		sueldo <- horasTrab * 20;
		Escribir "El sueldo que le corresponde esta semana es de: ",sueldo;
	SiNo
		horasExtra <- horasTrab - 40;
		sueldo <- (horasTrab - horasExtra) * 20;
		Escribir "El sueldo que le corresponde esta semana es de: ",sueldo + (horasExtra * 25);
	FinSi
FinFuncion	

Funcion tarea_07()	
	Escribir "7.    Hacer un algoritmo en Pseint para una tienda de helado que da un descuento por compra a sus clientes con membresía dependiendo de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:"
	
	Definir compra Como real;
	Definir tipoCliente como caracter;
	
	Escribir "Ingresar el monto a comprar: ";
	Leer compra;
	Escribir "Ingresar el tipo de cliente: A, B, C ";
	Leer tipoCliente;
	
	segun (tipoCliente) hacer
		Caso 'A':
			Escribir "Tipo de Cliente A";
			Escribir "Total a pagar: ",(compra - (compra * 0.10));
		Caso 'B':
			Escribir "Tipo de Cliente B";
			Escribir "Total a pagar: ",compra - (compra * 0.15);
		Caso 'C':
			Escribir "Tipo de Cliente C";
			Escribir "Total a pagar: ",compra - (compra * 0.20);
			
		De Otro Modo:
			Escribir "Total a pagar: ",compra;
	FinSegun
	
FinFuncion	

Funcion tarea_08()	
	
	Escribir "8.    Hacer un algoritmo en Pseint para calcular el promedio de tres notas y determinar si el estudiante aprobó o no."
	Definir nota1, nota2, nota3, promedio Como Real;
	promedio <- 0;
	
	Escribir "Recuerda que la mínima nota aprobatoria es 12";
	Escribir "Ingresar sus 3 notas:";
	Leer nota1, nota2, nota3;
	
	promedio <- (nota1 + nota2 + nota3) / 3;
	
	si (promedio >= 11.5) entonces
		Escribir " Estudiante Aprobado";
	SiNo
		Escribir "Estudiante Reprobado";
	FinSi
	
FinFuncion	

Funcion tarea_09()	
	Escribir "9.    Hacer un algoritmo en Pseint para determinar el aumento de un trabajador, se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%, si generaba menos de $2000 su aumento será de un 10%."
	Definir sueldo Como Real;
	
	Escribir 'Ingresar su sueldo anterior';
	
	Leer sueldo;
	
	Si (sueldo<2000) Entonces
		Escribir 'Su sueldo actual será de: ',sueldo+(sueldo*0.1);
	SiNo
		Escribir 'Su sueldo actual será de: ',sueldo+(sueldo*0.05);
	FinSi
	
FinFuncion	

Funcion tarea_10()	
	Escribir "10.    Hacer un algoritmo en Pseint que diga si un número es par o impar."
	escribir "Ingrese un numero para evaluar si es par o impar: "
	Leer n1
	si n1 % 2 == 0 Entonces
		Escribir "Este numero es par."
	SiNo
		Escribir "Este numero es impar."
	FinSi
	
FinFuncion	

Funcion tarea_11()	
	Escribir "11. Hacer un algoritmo en Pseint que lea tres números y diga cuál es el mayor."
	n_mayor = 0
	escribir "Ingrese el primer numero: "
	Leer n1
	si n1 > n_mayor Entonces
		n_mayor = n1		
	FinSi
	
	escribir "Ingrese el segundo numero: "
	Leer n2
	si n2 > n_mayor Entonces
		n_mayor = n2		
	FinSi
	
	escribir "Ingrese el tercer numero: "
	Leer n3
	si n3 > n_mayor Entonces
		n_mayor = n3		
	FinSi
	
	Escribir "El numero mayor es : " n_mayor
	
FinFuncion	

Funcion tarea_12()	
	Escribir "12. Hacer un algoritmo en Pseint que lea dos números y diga cuál es el mayor."
	n_mayor = 0
	escribir "Ingrese el primer numero: "
	Leer n1
	si n1 > n_mayor Entonces
		n_mayor = n1		
	FinSi
	escribir "Ingrese el segundo numero: "
	Leer n2
	si n2 > n_mayor Entonces
		n_mayor = n2		
	FinSi
	
	Escribir "El numero mayor es : " n_mayor
	
FinFuncion	

Funcion tarea_13()	
	Escribir "13. Hacer un algoritmo en Pseint que lea una letra y diga si es una vocal."
	
	Escribir "Escriba una letra: "
	leer letra
	
	Segun Minusculas(letra) Hacer
		"a":
			Escribir "La letra " letra " es una vocal"
		"e":
			Escribir "La letra " letra " es una vocal"
		"i":
			Escribir "La letra " letra " es una vocal"
		"o":
			Escribir "La letra " letra " es una vocal"
		"u":
			Escribir "La letra " letra " es una vocal"
		De Otro Modo:
			Escribir "La letra " letra " no es una vocal"
	Fin Segun
	
	
FinFuncion	

Funcion tarea_14()	
	Escribir "14. Hacer un algoritmo en Pseint que lea un entero positivo del 1 al diez y al 9 y determine si es un número primo."
	Escribir "Ingresa un número del 1 al 10";
	Leer num;
	
	si (num < 11 y num > 0) Entonces
		Segun (num) hacer
			caso 2: Escribir "El número es primo";
			caso 3: Escribir "El número es primo";
			caso 5: Escribir "El número es primo";
			caso 7: Escribir "El número es primo";
			De Otro Modo:
				Escribir "El número no es primo";
		FinSegun
	SiNo
		Escribir "No es un número del 1 al 10";
	FinSi
FinFuncion	

Funcion tarea_15()	
	Escribir "15. Hacer un algoritmo en Pseint que convierta centímetros a pulgadas y libras a kilogramos."
	Definir centimetros,pulgadas Como Real
	Definir kilo,libra Como Real
	
	Escribir "Ingresa el los centimetros por convertir a pulgadas."
	leer centimetros
	Escribir "Ingresa el peso en kilogramos por convertir a libras."
	leer kilo
	pulgadas = centimetros * 0.393701
	libra = kilo * 2.205
	Escribir "La conversión de centimetros a pulgadas es: ",pulgadas
	Escribir "La conversión de kilogramos a libras es: ",libra
	
FinFuncion	

Funcion tarea_16()	
	Escribir "16. Hacer un algoritmo en Pseint que lea un número y según ese número, indique el día que corresponde."
	escribir "Ingrese un numero del 1 al 7."
	Leer code_dia
	Segun code_dia Hacer
		1:
			Escribir "El dia equivalente al numero ingresado es Lunes."
		2:
			Escribir "El dia equivalente al numero ingresado es Marte."
		3:
			Escribir "El dia equivalente al numero ingresado es Miercoles."
		4:
			Escribir "El dia equivalente al numero ingresado es Jueves."
		5:
			Escribir "El dia equivalente al numero ingresado es Viernes."
		6:
			Escribir "El dia equivalente al numero ingresado es Sabado."
		7:
			Escribir "El dia equivalente al numero ingresado es Domingo."			
		De Otro Modo:
			Escribir "No esiste codificacion para este numero."	
	Fin Segun
FinFuncion	

Funcion tarea_17()	
	Escribir "17. Hacer un algoritmo en Pseint donde se ingrese una hora y nos calcule la hora dentro de un segundo."
	
	Hora_ = 0 
	Minutos_ = 0
	Segundos_ = 0
	Escribir "Escriba la horas: " Sin Saltar
	Leer Hora
	Escribir "Escriba los minutos: " Sin Saltar
	Leer Minutos_
	Escribir "Escriba los segundos: " Sin Saltar
	Leer Segundos_
		
	Escribir "La hora dentro de un segundo sera: " Hora ":" Minutos_ ":" Segundos_+1
FinFuncion	

Funcion tarea_18()	
	Escribir "18. Hacer un algoritmo en Pseint para una empresa se encarga de la venta y distribución de CD vírgenes. Los clientes pueden adquirir los artículos (supongamos un único producto de una única marca) por cantidad. Los precios son:"
	
	numeroCds = 0
	ganancia = 0
	precioTotal = 0
	
	Escribir "Numero de cds que comprara el cliente"
	Leer numeroCds
	
	Si numeroCds <= 9  Entonces
		precioTotal = numeroCds * 10
	FinSi
	
	Si numeroCds >= 10 & numeroCds <= 99 Entonces
		precioTotal = numeroCds * 8
	Fin Si
	
	Si numeroCds >= 100 & numeroCds <= 499  Entonces
		precioTotal = numeroCds * 7
	Fin Si
	
	Si numeroCds > 500  Entonces
		precioTotal = numeroCds * 6
	Fin Si
	
	Escribir "Precio total del cliente: ", precioTotal
	Escribir "Ganancia para el vendedor: " precioTotal*8.25/100
	
FinFuncion	

Funcion tarea_19()	
	Escribir "19. Hacer un algoritmo en Pseint para una heladería se tienen 4 tipos de empleados ordenados de la siguiente forma con su número identificador y salario diario correspondiente:"
	
	Definir  input2 Como Entero
	tarifa = 0
	input2 = 0
	ind_input1 = Falso
	
	Mientras ind_input1 = Falso
		escribir "Ingrese el tipo de empleado:"
		Escribir "Digita 1 para Cajero (56$/día)"
		Escribir "Digita 2 para Servidor (64$/día)"
		Escribir "Digita 3 para Preparador de mezclas (80$/día)"
		Escribir "Digita 4 para Mantenimiento (48$/día)"
		leer input1 
		Segun input1 Hacer
			1:
				input1 = input1
				tarifa = 56
				ind_input1 = Verdadero
			2:
				input1 = input1
				tarifa = 64
				ind_input1 = Verdadero
			3:
				input1 = input1
				tarifa = 80
				ind_input1 = Verdadero
			4:
				input1 = input1
				tarifa = 48
				ind_input1 = Verdadero
			De Otro Modo:
				Escribir "Opcion No valida para tipo de empleado."
				Escribir ""
				ind_input1 = Falso
				
		Fin Segun
	FinMientras

	ind_input2 = Falso
	Mientras ind_input2 = Falso
		escribir "Ingrese cantidad de dias laborados:"
		leer input2
		si input2 > 0 y input2 < 7 Entonces
			input2 = input2
			ind_input2 = Verdadero
		SiNo
			Escribir "La cantidad de dias no puede ser superior a 6 o igual a 0"
			Escribir ""
			ind_input2 = Falso
		FinSi
	FinMientras
	
	Escribir  "La cantidad a pagar al empleado es de : $/ ", tarifa * input2	
	
FinFuncion	

Funcion tarea_20()	
	
	Escribir "20. Hacer un algoritmo en Pseint que que lea 4 números enteros positivos y verifique y realice las siguientes operaciones:"
	Escribir ""
	regla_01 = Falso
	contador_pares = 0
	regla_02 = Verdadero	
	numero_mayor = 0
	regla_03 = Falso
	cuadrado_segundo = 0
	regla_04 = Falso
	media = 0
	regla_05 = Falso
	suma_numeros = 0
	
	Escribir "Ingrese 4 numeros enteros:"
	
	Escribir "Primer numero: "
	leer n1 
	si n1 % 2 == 0 Entonces
		contador_pares = contador_pares + 1
	FinSi
	si n1 > numero_mayor Entonces
		numero_mayor = n1
	FinSi
	
	Escribir "Segundo numero: "
	leer n2
	si n2 % 2 == 0 Entonces
		contador_pares = contador_pares + 1
	FinSi
	si n2 > numero_mayor Entonces
		numero_mayor = n2
	FinSi
	
	Escribir "Tercer numero: "
	leer n3 
	si n3 % 2 == 0 Entonces
		regla_03 = Verdadero
		contador_pares = contador_pares + 1
		cuadrado_segundo = n2^2
	FinSi
	si n3 > numero_mayor Entonces
		numero_mayor = n3
	FinSi
	
	Escribir "Cuardo numero: "
	leer n4 
	si n4 % 2 == 0 Entonces
		contador_pares = contador_pares + 1
	FinSi
	si n4 > numero_mayor Entonces
		numero_mayor = n4
	FinSi
	si n1<n4 Entonces
		regla_04 = Verdadero
		media = (n1 + n2 + n3 + n4)/4	
	FinSi
	
	si n2 > n3 Entonces
		si n3 >50 y n3 <700 Entonces
			regla_05 = Verdadero
			suma_numeros = (n1 + n2 + n3 + n4)
		FinSi
	FinSi
	si contador_pares <> 0 Entonces
		regla_01 = Verdadero
	FinSi
	
	si regla_01 = Verdadero Entonces
		Escribir "La cantidad de numeros pares encontrados es : ",contador_pares
	FinSi
	si regla_02 = Verdadero Entonces
		Escribir "El numero mayor es : ",numero_mayor
	FinSi
	si regla_03 = Verdadero Entonces
		Escribir "El cuadrado del segundo numero es : ",cuadrado_segundo
	FinSi
	si regla_04 = Verdadero Entonces
		Escribir "La media aritmetica de los 4 numeros es: ", media
	FinSi
	si regla_05 = Verdadero Entonces
		Escribir "La suma de los 4 numeros es: ", suma_numeros
	FinSi
	
FinFuncion	

Funcion tarea_21()	
	Escribir "21. Hacer un algoritmo en Pseint que permita calcular el factorial de un número."
	Definir num Como Entero
	Definir contador Como Entero
	Definir factorial Como Entero
	Escribir "Digite un numero entero:"
	Leer num;
	contador = 1
	factorial = 1
	Para contador=1 Hasta num Hacer 
		factorial = factorial*contador  
	FinPara
	Escribir "El factorial del numero ingresado es: ",factorial
	
FinFuncion	

Funcion tarea_22()	
	Escribir "22. Hacer un algoritmo en Pseint para calcular la suma de los n primeros números."
	Definir  input Como Entero
	suma = 0
	contador = 1
	Escribir "Ingrese un numero para sumar sus predecesores:"
	Leer input
	Para contador=1 Hasta (input - 1) Hacer 
		suma = suma + contador
	FinPara
	
	Escribir "La suma de los predecesores es: ", suma
	
FinFuncion

Funcion tarea_23()	//RESULETO
	Escribir "23. Hacer un algoritmo en Pseint para calcular la suma de los números impares menores o iguales a n."
	Escribir  ""
	Escribir "Ingrese un numero entero positivo:"
	Leer numeroEnteroIngresado
	count <- 0
	para i <- 1 Hasta numeroEnteroIngresado Con Paso 2 Hacer
		count <- count + i
	FinPara
	Escribir "La suma de los numeros es: ", count
FinFuncion	

Funcion tarea_24()	//RESUELTO
	Escribir "24. Hacer un algoritmo en Pseint para realizar la suma de todos los números pares hasta el 1000."
	count <- 0
	i <- 0
	Mientras i <= 1000 Hacer
		si i  % 2 == 0 Entonces
			count <- count + i
		FinSi
		i <- i + 1 
	FinMientras
	
	Escribir "La suma de los 1000 numeros pares es: ", count
	
FinFuncion	

Funcion tarea_25()	
	Escribir "25. Hacer un algoritmo en Pseint para calcular el factorial de un número de una forma distinta."
	contador<-1;
	factorial<-1
	Escribir "Digite un numero para calcular su factorial";
	Leer num;
	
	Mientras contador < num
		contador<-contador+1
		factorial<-factorial*contador
		
	FinMientras
	
	Escribir "El factorial de ",num," es ",factorial
FinFuncion	

Funcion tarea_26()	
	Escribir "26. Hacer un algoritmo en Pseint para calcular el resto y cociente por medio de restas sucesivas."
	
	Escribir "Ingrese el divisor:"
	Leer divisor
	Escribir "Ingrese el dividendo:"
	Leer dividendo
	
	cociente = 0
	
	Mientras divisor >= dividendo Hacer
		divisor = divisor - dividendo
		cociente = cociente +1
	FinMientras
	
	Escribir "El cociente es: ", cociente
	Escribir "El resto es: ", divisor
	
	
FinFuncion	

Funcion tarea_27()	
	Escribir "27. Hacer un algoritmo en Pseint para determinar la media de una lista indefinida de números positivos, se debe acabar el programa al ingresar un número positivo."
	Definir  C Como Entero
	definir x, suma Como Real
	
	x = 1
	suma = 0
	c= 0
	
	Mientras  x>=0 Hacer
		Escribir  "Ingresa cualquier numero positivo."
		Leer  x
		si x >= 0 Entonces
			suma = suma + x
			c = c + 1
		FinSi
	FinMientras
	
	si c > 0 Entonces
		Escribir  "La media es: ", suma / c
	FinSi
	
FinFuncion	
Funcion tarea_28()	
	Escribir "28. Hacer un algoritmo en Pseint para calcular la suma de los primeros cien números con un ciclo repetir."
	count = 1
	suma = 0
	Repetir
		suma = suma + count
		count = count + 1
	Hasta Que count == 101
	
	Escribir  "(ciclo Repetir) La suma de 1 a 100 es : " suma
	
FinFuncion	

Funcion tarea_29()	
	Escribir "29. Hacer un algoritmo en Pseint para calcular la suma de los primeros cien números con un ciclo mientras."
	count = 1
	suma = 0
	mientras count <= 100 Hacer
		suma = suma + count
		count = count + 1
	FinMientras
	Escribir "(Ciclo Mientras) La suma de 1 a 100 es: " suma
FinFuncion	

Funcion tarea_30()	
	Escribir "30. Hacer un algoritmo en Pseint para calcular la suma de los primeros cien números con un ciclo para."
	suma = 0
	para i <- 1 hasta 100 Con Paso 1 Hacer
		suma <- suma + i
	FinPara
	
	Escribir "(Ciclo Para) La suma de 1 a 100 es : " suma
FinFuncion	

Funcion tarea_31()	
	Escribir "31. Hacer un algoritmo en Pseint parar calcular la media de los números pares e impares, sólo se ingresará diez números."
	Dimension array[10]
	numeroAcumulado_Par = 0
	pares = 0
	numeroAcumulado_Impar = 0
	impares = 0
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Leer array[i]
		Si array[i]%2==0 Entonces
			numeroAcumulado_Par = numeroAcumulado_Par + array[i]
			pares = pares + 1
		SiNo
			numeroAcumulado_Impar = numeroAcumulado_Impar + array[i]
			impares = impares +1
		Fin Si
		
		
	Fin Para
	
	Escribir  "Media de pares: " numeroAcumulado_Par/pares
	Escribir  "Media de impares: " numeroAcumulado_Impar/impares
FinFuncion	

Funcion tarea_32()	
	Escribir "32. Se quiere saber cuál es la ciudad con la población de más personas, son tres provincias y once ciudades, hacer un algoritmo en Pseint que nos permita saber eso."
	Dimension PersonasXCiudad[11]
	Ciudad_Mas_Habitantes = 0
	Para i<-1 Hasta 11 Con Paso 1 Hacer
		Leer PersonasXCiudad[i]
		
		Si PersonasXCiudad[i] > Ciudad_Mas_Habitantes  Entonces
			Ciudad_Mas_Habitantes = PersonasXCiudad[i]
		Fin Si
		
	Fin Para
	
	Escribir "La ciudad con mas habitantes tiene ", Ciudad_Mas_Habitantes, " habitantes"
FinFuncion	

Funcion tarea_33()	
	Escribir "33. Hacer un algoritmo en Pseint que permita al usuario continuar con el programa."
	input = ""
	Mientras input <> "N" & input <> "n"  Hacer
		Escribir "Quieres continuar con el programa"
		Escribir "(Any)Si"
		Escribir "(N)No"
		Leer input
		
	Fin Mientras
	
FinFuncion	

Funcion tarea_34()	
	Escribir "34. Hacer un algoritmo en Pseint que imprima la tabla de multiplicar de los números del uno nueve."
	Para i <- 0 Hasta 9 Con Paso 1 Hacer
		Escribir "Tabla de Multiplicacion del: ", i
		Para j <- 0 Hasta 9 Con Paso 1 Hacer
			Escribir i " x " j " = " i*j
		Fin Para
	Fin Para
	
FinFuncion	

Funcion tarea_35()	
	Escribir "35. Hacer un algoritmo en Pseint que nos permita saber cuál es el número mayor y menor, se debe ingresar sólo veinte números."
	Dimension Numeros_Ingresados[5]
	
	
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Leer Numeros_Ingresados[i]
	Fin Para
	numeroMayor = Numeros_Ingresados[1]
	numeroMenor = Numeros_Ingresados[1]
	
	
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Si Numeros_Ingresados[i] > numeroMayor  Entonces
			numeroMayor = Numeros_Ingresados[i]
		Fin Si
		
		Si Numeros_Ingresados[i] < numeroMenor  Entonces
			numeroMenor = Numeros_Ingresados[i]
		Fin Si
		
	Fin Para
	
	
	Escribir numeroMayor
	Escribir numeroMenor
	
FinFuncion	

Funcion tarea_36()	
	Escribir "36. Hacer un algoritmo en Pseint para calcular la serie de Fibonacci."
	
	NumeroDeDigitosEnSerie = 0
	numeroAcumulado = 0
	N_Anterior = 0
	N_Actual = 1
	
	Escribir  "Cuantos terminos tendra la sucesion?"
	Leer  NumeroDeDigitosEnSerie
	
	Si NumeroDeDigitosEnSerie == 1 | NumeroDeDigitosEnSerie == 2 Entonces
		Escribir 1
	SiNo
		Para i <- 0 Hasta NumeroDeDigitosEnSerie-2 Con Paso 1 Hacer
			
			numeroAcumulado = N_Anterior + N_Actual
			N_Anterior = N_Actual
			N_Actual = numeroAcumulado
			
		Fin Para
		
		Escribir numeroAcumulado
	Fin Si
	
FinFuncion	

Funcion tarea_37()	
	Escribir "37. Hacer un algoritmo en Pseint para conseguir el M.C.D de un número por medio del algoritmo de Euclides."
	Escribir "El M.C.D. entre 1 y 12 es: " mcdRecursivo(1,12)
	
FinFuncion	

Funcion mcd_ <- mcdRecursivo (a, b)
	Si a < b Entonces
		mcd_ <- mcdRecursivo(b,a)
	SiNo
		Si b == 0 Entonces
			mcd_ <- a
		SiNo
			mcd_ <- mcdRecursivo(b,a%b)
		Fin Si
	Fin Si
	
Fin Funcion

Funcion tarea_38()	
	Escribir "38. Hacer un algoritmo en Pseint que nos permita saber si un número es un número perfecto."
	
	numeroPerfecto_ = 0
	acumulador = 0
	Escribir "Inserte numero para comprobar si es perfecto"
	Leer numeroPerfecto_
	
	
	Para i <- 1 Hasta numeroPerfecto_-1 Con Paso 1 Hacer
		Si numeroPerfecto_ % i == 0 Entonces
			acumulador = acumulador + i
		SiNo
			
		Fin Si
	Fin Para
	
	
	Si numeroPerfecto_ == acumulador Entonces
		Escribir "Es un numero perfecto"
	SiNo
		Escribir "No es un numero perfecto"
	Fin Si
	
FinFuncion	

Funcion tarea_39()	
	Escribir "39. Hacer un algoritmo en Pseint que cumpla con la aproximación del número pi con la serie de Gregory-Leibniz. La formula que se debe aplicar es:"
	i = 0
	iteraciones_max = 9999
	
	
	pi_value = 0 
	denominador = 1
	signo = 1
	
	Mientras i<iteraciones_max Hacer
		pi_value = pi_value  + (4/denominador * signo)
		
		denominador = denominador + 2
		signo = signo * (-1)
		i = i + 1
	Fin Mientras
	
	Escribir pi_value
FinFuncion	

Funcion tarea_40()	
	Escribir "40. Hacer un algoritmo en Pseint que cumpla con la aproximación del número pi con la serie de Nilakantha. La formula que se debe aplicar es:"
	
	i = 0
	iteraciones_max = 0
	
	
	pi_value = 3 
	denominador = 2
	signo = 1
	
	
	Mientras i<iteraciones_max Hacer
		pi_value = pi_value  + ((4/(denominador*(denominador+1)*(denominador+2))) * signo)
		denominador = denominador + 2
		signo = signo * (-1)
		i = i + 1
	Fin Mientras
	
	Escribir pi_value
	
	
FinFuncion	



