Proceso e32
	Definir poblacion, max_poblacion, ciudad_mas_grande como Entero
	max_poblacion <- 0
	
	Para i <- 1 Hasta 11 Con Paso 1 Hacer
		Escribir"Ingrese la población de la ciudad ", i, ": "
		Leer poblacion
		Si (poblacion > max_poblacion) Entonces
			max_poblacion <- poblacion
			ciudad_mas_grande <- i
		Fin Si
	Fin Para
	
	Escribir"La ciudad con la población más grande es la ciudad ", ciudad_mas_grande, " con una población de ", max_poblacion, " habitantes."

	
FinProceso
