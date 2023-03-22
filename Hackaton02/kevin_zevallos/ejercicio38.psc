Algoritmo ejercicio38
	Escribir "Ingrese un número: "
	Leer num
	suma_divisores = 0
	
	Para i = 1 Hasta num - 1 Con Paso 1 Hacer
		Si num MOD i = 0 Entonces
			suma_divisores = suma_divisores + i
		Fin Si
	Fin Para
	
	Si suma_divisores = num Entonces
		Escribir num, " es un número perfecto"
	Sino
		Escribir num, " no es un número perfecto"
	Fin Si


FinAlgoritmo

