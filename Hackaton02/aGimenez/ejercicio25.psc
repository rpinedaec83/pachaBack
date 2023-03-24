Proceso ejercicio25
	factorial = 0
	numero1 = 0
	
	Escribir "Ingrese un numero"
	Leer numero1 
	si numero1 < 0 Entonces
		Escribir "El numero " numero1 " no se puede calcular"
	SiNo
		x = 1
		factorial = 1
		Repetir
			factorial = factorial * x
			x = x + 1
		Hasta Que x > numero1
		Escribir "El factorial de " numero1 " es " factorial 
	FinSi
	
FinProceso
