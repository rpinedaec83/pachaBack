Algoritmo VerificarPerfecto
	n = 0
	j = 0
	Escribir "Ingresar un número: "
	leer n
	i = 2
	suma = 0
	Mientras i <= n Hacer
		Si n mod i = 0 Entonces
			j = n/i
			suma = suma + j
		FinSi
		i = i + 1
	FinMientras
	Si suma = n Entonces
		Escribir "El numero es perfecto"
	SiNo
		Escribir "El numero no es perfecto"
	FinSi
FinAlgoritmo
