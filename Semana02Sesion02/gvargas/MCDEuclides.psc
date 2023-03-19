Algoritmo MCDEuclides
	num1 = 0
	num2 = 0
	a = 0
	b = 0
	res = 0
	Escribir "Ingrese el primer número: "
	Leer num1
	Escribir "Ingrese el segundo número: "
	Leer num2
	Si num1 > num2 Entonces
		a = num2
		b = num1
	SiNo
		a = num1
		b = num2
	FinSi
	Mientras b <> 0 Hacer
		res = b 
		b = a mod b
		a = res
	FinMientras
	Escribir "El MCD es: " res
FinAlgoritmo
