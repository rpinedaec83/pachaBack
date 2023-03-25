Algoritmo ejercicio38
	//Hacer un algoritmo en Pseint que nos permita saber si un número es un número perfecto.
	numeroPerfecto_ = 0
	acumulador = 0
	Escribir "Inserte numero para comprobar si es perfecto"
	Leer numeroPerfecto_
	
	
	Para i <- 1 Hasta numeroPerfecto_-1 Con Paso 1 Hacer
		Si numeroPerfecto_ % i == 0 Entonces
			acumulador = acumulador + i
		SiNo
			
		Fin Si
	Fin Para
	
	
	Si numeroPerfecto_ == acumulador Entonces
		Escribir "Es un numero perfecto"
	SiNo
		Escribir "No es un numero perfecto"
	Fin Si
FinAlgoritmo
