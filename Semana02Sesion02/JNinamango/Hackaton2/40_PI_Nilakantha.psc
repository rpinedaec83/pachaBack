Algoritmo PI_Nilakantha
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
