Algoritmo MayorYMenor
	num = 0
	i = 0
	may = 0
	men = 999999
	Mientras i < 20 Hacer
		Escribir "Ingresar el número: "
		Leer num
		Si num < men Entonces
			men = num
		FinSi
		Si num > may Entonces
			may = num
		FinSi
		i = i + 1
	FinMientras
	Escribir "El número menor es: " men
	Escribir "El número mayor es: " may
FinAlgoritmo
