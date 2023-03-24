Algoritmo NumeroPerfecto
	Escribir "Ingrese un número:"
	Leer n
	suma <- 0
	Para i <- 1 Hasta n/2 Con Paso 1 Hacer
		Si n mod i = 0 Entonces
			suma <- suma + i
		Fin Si
	Fin Para
	Si suma = n Entonces
		Escribir n, " es un número perfecto."
		SiNo
			Escribir n, " no es un número perfecto."
	Fin Si
Fin Algoritmo
