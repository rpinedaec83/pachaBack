Algoritmo e25
	
	Definir num, factorial, i como Entero
	
	Escribir "Ingrese un número entero positivo: "
	Leer num
	
	factorial <- 1
	i <- 1
	
	Mientras i <= num Hacer
		factorial <- factorial * i
		i <- i + 1
	FinMientras
	
	Escribir "El factorial de ", num, " es: ", factorial
	
FinAlgoritmo
