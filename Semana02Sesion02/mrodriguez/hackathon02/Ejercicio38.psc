Proceso Ejercicio38
	//Hacer un algoritmo en Pseint que nos permita 
	//saber si un número es un número perfecto.

	num = 0
	acum = 0
	Escribir "Ingresa un numero para saber si es perfecto"
	Leer num
	
	Para i <- 1 Hasta num - 1 Con Paso 1 Hacer
		Si num % i == 0 Entonces
			acum = acum + i
		SiNo
		Fin Si
	Fin Para
	
	Si num == acum Entonces
		Escribir num " es un numero perfecto"
	SiNo
		Escribir num " No es un numero perfecto"
	Fin Si
FinProceso
