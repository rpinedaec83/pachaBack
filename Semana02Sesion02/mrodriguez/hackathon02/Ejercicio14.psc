Proceso Ejercicio14
	//Hacer un algoritmo en Pseint que
	//lea un entero positivo del 1 al diez
	//y al 9 y determine si es un n�mero primo.

	Escribir "Ingresa un numero de 1 al 10:"
	leer num

	count <- 0

	Para i <- 1 Hasta num Hacer
		si num % i = 0 Entonces
			count <- count + 1
		FinSi
	FinPara

	si count = 2 Entonces
		Escribir num " es n�mero primo"
	SiNo
		Escribir num " NO es n�mero primo"
	FinSi

FinProceso
