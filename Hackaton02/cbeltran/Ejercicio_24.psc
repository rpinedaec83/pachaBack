Proceso Suma_numeros_pares
	i=0
	suma=0 
	
	i = 0
	suma = 0
	
	Mientras i <= 1000 Hacer
		Si i % 2 == 0 Entonces
			suma = suma + i
		FinSi
		i = i + 1
	FinMientras
	Escribir "La suma de todos los numeros pares hasta el 1000 es: ", suma
FinProceso
