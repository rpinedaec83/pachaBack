Proceso Ejercicio40
	//Hacer un algoritmo en Pseint que cumpla
	//con la aproximaci�n del n�mero pi con la serie de Nilakantha. 
	//La formula que se debe aplicar es:

	// Pi = = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...

	i = 0
	iteraciones_max = 9999

	pi_value = 3
	denominador = 2
	signo = 1

	Mientras i < iteraciones_max Hacer
		pi_value = pi_value + ((4 / (denominador * (denominador + 1) * (denominador + 2))) * signo)
		denominador = denominador + 2
		signo = signo * (-1)
		i = i + 1
	Fin Mientras
	Escribir pi_value
FinProceso
