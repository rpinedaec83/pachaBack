Algoritmo Ejercicio26
	//Hacer un algoritmo en Pseint para calcular el
	//resto y cociente por medio de restas sucesivas.

	Escribir "Primer n�mero"
	Leer a
	Escribir "Segundo n�mero"
	Leer b

	Cociente <- 0
	Mientras a >= b Hacer
		a <- a - b
		cociente <- cociente + 1
	FinMientras
	Escribir "El cociente es: " , cociente
	Escribir "El resto es : " , a
FinAlgoritmo

