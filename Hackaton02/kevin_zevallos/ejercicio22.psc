Algoritmo ejercicio22
	Escribir "Ingrese un número entero positivo:"
	Leer num
	factorial <- 1
	Si num == 0 Entonces
		factorial = 1
	SiNo
		Para i <- 1 Hasta num
			factorial <- factorial * i
		Fin Para
	FinSi
	Escribir "El factorial de ", num, " es: ", factorial
FinAlgoritmo