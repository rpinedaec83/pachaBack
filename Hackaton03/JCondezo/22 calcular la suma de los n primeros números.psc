//
Algoritmo sin_titulo
	Definir total,x Como Entero
	Definir suma,n Como Real
	Escribir "Cuantos numeros deseas sumar"
	leer total
	x = 1
	suma = 0
	Mientras  x <= total Hacer
		Escribir "Ingresa un numero "
		leer n
		suma = suma + n
		x = x + 1
	FinMientras
	Escribir "La suma de los ",total," numeros es: ",suma
FinAlgoritmo
