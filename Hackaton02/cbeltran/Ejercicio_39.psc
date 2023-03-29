Proceso Gregory_Leibniz_pi

	num=0
	num_pi = 0.0
	contador = 0
	
	Escribir "Ingrese un número: "
	Leer num
	
	para i = 1 hasta num con paso 2 hacer
		
		si (contador mod 2 = 0) Entonces
			num_pi = num_pi + (4 / i)
		Sino
			num_pi = num_pi - (4/ i)
		FinSi
		contador = contador + 1
		
	FinPara
	
	Escribir "Pi se aproxima a: " num_pi
FinProceso
