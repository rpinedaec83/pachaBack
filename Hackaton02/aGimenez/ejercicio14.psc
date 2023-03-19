Proceso ejercicio14
	numero1 = 0
	contador = 0
	x = 1
	
	Escribir "Ingrese un numero"
	Leer numero1
	
	Mientras  x <= numero1 Hacer
		si numero1 mod x == 0 Entonces
			contador = contador + 1
		FinSi
		x = x + 1
	FinMientras
	
	si contador == 2 o numero1 == 1 Entonces
		Escribir "El numero " numero1 " es primo"
	SiNo
		Escribir "El numero " numero1 " no es primo"
	FinSi

FinProceso
