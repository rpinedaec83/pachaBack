Algoritmo ejercicio24
	//Hacer un algoritmo en Pseint para realizar la suma de todos los números pares hasta el 1000.
	count <- 0
	i <- 0
	
	Mientras i <= 1000 Hacer
		si i% 2 == 0 Entonces
			count <- count
		FinSi
		i <- i + 1
	FinMientras

	Escribir "la suma de los 1000 numeros pares es: ", count
FinProceso