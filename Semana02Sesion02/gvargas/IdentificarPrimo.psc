Algoritmo IdentificarPrimo
	num = 0
	i = 1
	j = 0
	Escribir "Escriba un número positivo entre 1 y 10: "
	Leer num
	Si num > 0 y num < 11 Entonces
		Mientras i <= num Hacer
			Si num mod i = 0 Entonces
				j = j + 1
			FinSi
			i = i + 1
		FinMientras
		Si j = 2 Entonces
			Escribir "El número es primo"
		SiNo
			Escribir "El número no es primo"
		FinSi
	SiNo
		Escribir "El número está fuera de rango"
	FinSi
FinAlgoritmo
