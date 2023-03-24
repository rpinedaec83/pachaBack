Algoritmo ejer27
	//Hacer un algoritmo en Pseint para calcular el resto y cociente por medio de restas sucesivas.
	Escribir "Ingrese el dividendo:"
	Leer dividendo
	Escribir "Ingrese el divisor:"
	Leer divisor
	cociente = 0
	resto = 0
	Mientras dividendo >= divisor Hacer
		dividendo = dividendo - divisor
		cociente = cociente + 1
	FinMientras
	resto = dividendo
	Escribir "El cociente es:", cociente
	Escribir "El resto es:", resto
FinAlgoritmo
