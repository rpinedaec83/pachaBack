//Hacer un algoritmo en Pseint para determinar la media de una lista indefinida de números positivos, se debe acabar el programa al ingresar un número positivo.
Proceso Ejercicio27
	Definir c Como Entero
	Definir x, suma Como Real
	x=1
	suma=0
	C=0
	Mientras x>=0 Hacer
		Escribir "Ingresa cualquier numero positivo "
		leer x
		si x>=0 Entonces
			suma=suma+x
			C=C+1
		FinSi
	FinMientras
	si C>0 Entonces
		Escribir "La media es " suma/C
	FinSi
	
FinProceso
