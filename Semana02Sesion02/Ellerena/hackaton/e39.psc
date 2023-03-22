Algoritmo e39
	
	Escribir "Ingrese la cantidad de términos a utilizar en la aproximación:"
	Leer n
	
	pe = 0
	signo = 1
	
	Para i = 1 Hasta n Con Paso 1 Hacer
		termino = 4 / (2 * i - 1)
		pe = pe + signo * termino
		signo = -signo
	FinPara
	
	Escribir "El valor aproximado de pi con ", n, " términos es: ", pi
	
FinAlgoritmo
