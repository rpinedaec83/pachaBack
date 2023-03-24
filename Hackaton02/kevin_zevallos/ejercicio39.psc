Algoritmo ejercicio39
	Escribir "Ingrese el número de términos para aproximar pi: "
	Leer n
	
	p = 0
	signo = 1
	
	Para i = 1 Hasta n Con Paso 1 Hacer
		termino = signo / (2 * i - 1)
		p = p + termino
		signo = signo * (-1)
	Fin Para
	
	p = p * 4
	
	Escribir "La aproximación de pi es: ", pi


FinAlgoritmo

