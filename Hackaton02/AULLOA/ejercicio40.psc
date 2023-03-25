Algoritmo ejercicio40
	//Hacer un algoritmo en Pseint que cumpla con la aproximación del número pi con la serie de Nilakantha. La formula que se debe aplicar es:
	//Pi = = 3 + 4/(234) - 4/(456) + 4/(678) - 4/(8910) + 4/(101112) - (4/(121314) ...
	i = 0
	iteraciones_max = 0
	
	
	pi_value = 3 
	denominador = 2
	signo = 1
	
	
	Mientras i<iteraciones_max Hacer
		pi_value = pi_value  + ((4/(denominador*(denominador+1)*(denominador+2))) * signo)
		denominador = denominador + 2
		signo = signo * (-1)
		i = i + 1
	Fin Mientras
	
	Escribir pi_value
	
	
FinAlgoritmo