Proceso Factorial_distinto
	
	num=0
	factorial=1
	
    Escribir "Ingrese un número para calcular su factorial: "
    Leer num
	
    Mientras num > 0
        factorial = factorial * num
        num = num - 1   
    FinMientras
    
    Escribir "El factorial del número ingresado es: ", factorial
FinProceso
