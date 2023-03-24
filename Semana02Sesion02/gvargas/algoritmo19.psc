Algoritmo Algoritmo19
	num1 = 0
	num2 = 0
	num3 = 0
	num4 = 0
	i = 0
	Escribir "Escriba el número 1: "
	Leer num1
	Escribir "Escriba el número 2: "
	Leer num2
	Escribir "Escriba el número 3: "
	Leer num3
	Escribir "Escriba el número 4: "
	Leer num4
	Si num1 mod 2 = 0 Entonces
		i = i + 1
	FinSi
	Si num2 mod 2 = 0 Entonces
		i = i + 1
	FinSi
	Si num3 mod 2 = 0 Entonces
		i = i + 1
	FinSi
	Si num4 mod 2 = 0 Entonces
		i = i + 1
	FinSi
	Escribir i " números son pares"
	i = 1
	j = 1
	men = num1
	Mientras i <= 4 Hacer
		Segun i Hacer
			1: 
				numi = num1
			2: 
				numi = num2
			3: 
				numi = num3
			4: 
				numi = num4
		FinSegun
		Si numi > men Entonces
			men = numi
		FinSi
		i = i + 1
	FinMientras
	Escribir "El mayor número es " men
	Si num3 mod 2 = 0 Entonces
		Escribir "El cuadrado del segundo número es: " num2^2
	FinSi
	prom = 0
	Si num1 < num4 Entonces
		prom = (num1 + num2 + num3 + num4)/4
		Escribir "La media de los números es: " prom
	FinSi
	Si num2 < num3 Entonces
		suma = 0
		Si num3 > 50 y num3 <700 Entonces
			suma = num1 + num2 + num3 + num4
			Escribir "La suma de los números es: " suma
		FinSi
	FinSi
FinAlgoritmo
