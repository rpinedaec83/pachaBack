Proceso ejercicio35
	Definir contador, numero1, numeroMayor, numeroMenor Como Entero
	contador = 0
	numeroMayor = 0
	numeroMenor = 99999
	Mientras contador <> 21 Hacer
		Escribir "Ingrese un numero"
		Leer numero1
		si numero1 < numeroMenor Entonces
			numeroMenor = numero1
		FinSi
		si numero1 > numeroMayor Entonces
			numeroMayor = numero1
		FinSi
		contador = contador + 1
	FinMientras
	Escribir "El numero Menor es: " numeroMenor
	Escribir "El numero Mayor es: " numeroMayor
FinProceso
