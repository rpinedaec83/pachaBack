Algoritmo PiGregoryLeibniz
	iteraciones = 10
	Escribir "Escribir el número de iteraciones: "
	Leer iteraciones
	numerador = 4
	denominador = 1
	p = 0
	x = 0
	operador = 1
	Mientras x < iteraciones Hacer
		p = operador * (numerador / denominador)
		denominador = denominador + 2
		operador = operador + 1
		x = x + 1
	FinMientras
	Escribir "Se obtuvo que pi es igual a: " p
FinAlgoritmo
