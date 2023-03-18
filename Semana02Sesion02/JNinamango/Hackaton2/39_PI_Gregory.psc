Algoritmo PI_
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
