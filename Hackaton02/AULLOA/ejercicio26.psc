Algoritmo ejercicio26
	//Hacer un algoritmo en Pseint para calcular el resto y cociente por medio de restas sucesivas.
	Escribir "primer numero"
	Leer a
	Escribir "segundo numero"
	Leer b
	Cociente <- 0
	Mientras a>=b Hacer
		a <- b - b
		cociente <- cociente + 1
	FinMientras
	Escribir "cociente: ", cociente
	Escribir "resto: ", a
FinAlgoritmo