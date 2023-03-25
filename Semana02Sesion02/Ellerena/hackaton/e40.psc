Algoritmo e40
	
	Definir n Como Entero
	Definir i, signo Como Entero
	Definir pe, termino Como Real
	
	Escribir "Ingrese la cantidad de términos a utilizar en la aproximación:"
	Leer n
	
	pe = 3.0
	signo = 1
	
	Para i = 2 Hasta n*2 Con Paso 2 Hacer
		termino = 4.0 / ((i-1) * i * (i+1))
		pe = pe + signo * termino
		signo = -signo
	FinPara
	
	Escribir "El valor aproximado de pi con ", n, " términos es: ", pi
	
FinAlgoritmo
