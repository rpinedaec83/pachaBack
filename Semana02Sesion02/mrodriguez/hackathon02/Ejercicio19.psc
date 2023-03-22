Algoritmo Ejercicio19
	//Hacer un algoritmo en Pseint para una helader�a se tienen 4 tipos de empleados
	//ordenados de la siguiente forma con su n�mero identificador y salario diario correspondiente:

	//01. Cajero (56$/d�a).
	//02. Servidor (64$/d�a).
	//03. Preparador de mezclas (80$/d�a).
	//04. Mantenimiento (48$/d�a).

    //El due�o de la tienda desea tener un programa donde
	//s�lo ingrese dos n�meros enteros que representen al n�mero identificador del empleado 
	//y la cantidad de d�as que trabaj� en la semana (6 d�as m�ximos).
	//Y el programa le mostrar� por pantalla la cantidad de dinero
	//que el due�o le debe pagar al empleado que ingres�

	Escribir "Ingresar identificador de empleado (2 d�gitos): "
	leer tipo

//	si longitud(tipo) == 2 Entonces
		Escribir "Ingresar numero de dias trabajados: "
		leer diasTrabajados
		si diasTrabajados <= 6 Entonces
			Segun tipo Hacer
				01: Escribir "Monto total a pagar al cajero por ", diasTrabajados, " d�as es: " diasTrabajados*56
				02: Escribir "Monto total a pagar al servidor por ", diasTrabajados, " d�as es: " diasTrabajados*64
				03: Escribir "Monto total a pagar al preparador por ", diasTrabajados, " d�as es: " diasTrabajados*80
				04: Escribir "Monto total a pagar al mantenimiento por ", diasTrabajados, " d�as es: " diasTrabajados*48
			FinSegun
		SiNo
			Escribir "Numero de dias excede a 6: ", diasTrabajados
		FinSi
//	SiNo
//		Escribir "Identificador incorrrecto"
//	FinSi
FinAlgoritmo
