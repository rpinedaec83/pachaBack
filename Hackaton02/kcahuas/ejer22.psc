Algoritmo ejer22
	Escribir "Ingrese un número entero positivo: "
	Leer n
	Si n <= 0 Entonces
		Escribir "El número ingresado debe ser positivo."
	Sino
		suma <- 0
		Para i <- 1 Hasta n Con Paso 1 Hacer
			suma <- suma + i
		FinPara
		Escribir "La suma de los primeros ", n, " números es: ", suma
	FinSi
FinAlgoritmo
