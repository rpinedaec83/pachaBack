Algoritmo Ejercicio27
	//Hacer un algoritmo en Pseint para determinar
	//la media de una lista indefinida de n�meros positivos,
	//se debe acabar el programa al ingresar un n�mero negativo.

	Definir c Como Entero
	Definir x, suma Como Real
	x = 1
	suma =0
	c = 0

	Mientras x >= 0 Hacer
		Escribir "Ingresa un n�mero positivo"
		Leer x
		si x >= 0 Entonces
			suma = suma + x
			c = c + 1
		FinSi
	FinMientras
	si c > 0 Entonces
		Escribir "La media de los n�meros positivos es: " , suma / c
	FinSi
FinAlgoritmo

