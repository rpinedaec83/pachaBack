Algoritmo ejericico_26
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
	
	
FinAlgoritmo
