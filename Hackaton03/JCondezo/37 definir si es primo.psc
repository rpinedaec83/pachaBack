//definir si numero es primo
Algoritmo sin_titulo
	Definir n,x,perfecto Como Entero
		Escribir "Ingresa un numero"
	leer n
	x = 2
	perfecto = 0
		Mientras x <= n Hacer
		si n mod x == 0 Entonces
			perfecto = perfecto + (n/x)
		FinSi
		x = x + 1
		FinMientras
		si perfecto == n Entonces
		Escribir "El numero",n, "es un numero perfecto"
			SiNo
				Escribir "el numero ",n," no es un numero ferfecto"
		
	FinSi
FinAlgoritmo
