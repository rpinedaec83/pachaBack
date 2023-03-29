Proceso Ejercicio17
	//Hacer un algoritmo en Pseint donde
	//se ingrese una hora y nos calcule
	//la hora dentro de un segundo
	Definir h, m, s Como Entero

	Escribir "Ingresar hora"
	leer h
	Escribir "Ingresar minuto"
	leer m
	Escribir "Ingresar segundo"
	leer s

	si (h < 24 y m < 60 y s < 60) Entonces
		s <- s + 1
		si s = 60 Entonces
			s <- 0
			m <- m + 1
			si m = 60 Entonces
				m <- 0
				h <- h + 1
				si h = 24 Entonces
					h <- 0
				FinSi
			FinSi
		FinSi
	FinSi
	Escribir h, " : " m " : " s
FinProceso
