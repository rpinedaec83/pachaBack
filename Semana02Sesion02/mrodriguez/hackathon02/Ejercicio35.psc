Proceso Ejercicio35
	//Hacer un algoritmo en Pseint que nos permita
	//saber cu�l es el n�mero mayor y menor,
	//se debe ingresar s�lo veinte n�meros.

	Para i <- 1 Hasta 20 Hacer
		Escribir "El numero es ", i , ":"
		leer numeroIngresado

		si numeroIngresado > mayor Entonces
			mayor <- numeroIngresado
		FinSi
		si numeroIngresado < menor Entonces
			menor <- numeroIngresado
		FinSi
	Fin Para
	Escribir "El numero mayor es: ", mayor
	Escribir "El numero menor es: ", menor
FinProceso
