Algoritmo SumaNImpares
	n = 0
	suma = 0
	i = 1
	Escribir "Insertar n: "
	Leer n
	Mientras i <= n Hacer
		Si i mod 2 <> 0 Entonces
			suma = suma + i
		FinSi
		i = i + 1
	FinMientras
	Escribir "La suma de los " n " primeros números impares es " suma
FinAlgoritmo
