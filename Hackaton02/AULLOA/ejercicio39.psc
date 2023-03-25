Algoritmo ejercicio39
	//Hacer un algoritmo en Pseint que cumpla con la aproximación del número pi con la serie de Gregory-Leibniz. La formula que se debe aplicar es:
	//Pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
	i = 0
	iteraciones_max = 9999
	
	
	pi_value = 0 
	denominador = 1
	signo = 1
	
	Mientras i<iteraciones_max Hacer
		pi_value = pi_value  + (4/denominador * signo)
		
		denominador = denominador + 2
		signo = signo * (-1)
		i = i + 1
	Fin Mientras
	
	Escribir pi_value
FinAlgoritmo