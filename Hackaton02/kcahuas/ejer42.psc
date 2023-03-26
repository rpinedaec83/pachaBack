Algoritmo ejer42
	//Hacer un algoritmo en Pseint que cumpla con la aproximación del número pi con la serie de Nilakantha. La formula que se debe aplicar es:
	
	//Pi = = 3 + 4/(234) - 4/(456) + 4/(678) - 4/(8910) + 4/(101112) - (4/(121314) ...
	Definir n, i Como Entero
	definir sig Como Entero
	Definir signo Como Entero
	sig = 3

	signo = 1
	denominador = 2
	
	Escribir "Ingrese el número de términos de la serie:"
	Leer n
	
	Para i = 1 Hasta n Hacer
		sig = sig + signo * (4 / (denominador * (denominador + 1) * (denominador + 2)))
		denominador = denominador + 2
		signo = (signo *( -1))
	FinPara
	
	Escribir "La aproximación de pi es: ", pi
FinAlgoritmo
