Proceso calculadora 
	Numero1 = 0
	Numero2 = 0
	Operacion= ""
	Resultado= 0 
	Escribir "Ingresa el primer numero"
	leer Numero1
	Escribir "Ingresa el siguiente numero"
	leer Numero2 
	Escribir "Ingresa el tipo de operacion (suma, resta, multiplicacion o division)"
	leer Operacion
	
	si Operacion == "Suma" Entonces
		Resultado= Numero1 + Numero2
		Escribir "La suma de " Numero1 " y " Numero2 " es: " Resultado	
	Sino 
		si Operacion == "resta" Entonces
		Resultado= Numero1 - Numero2
		Escribir "La resta de " Numero1 " y " Numero2 " es: " Resultado	
	Sino 
		si Operacion == "multiplicacion" Entonces
			Resultado= Numero1 * Numero2
			Escribir "La multiplicacion de " Numero1 " y " Numero2 " es: " Resultado	
	Sino 
		si Operacion == "division" Entonces
			Resultado= Numero1 / Numero2
			Escribir "La division de " Numero1 " y " Numero2 " es: " Resultado	
				
				FinSi		
			FinSi	
		FinSi
	Finsi
	
	
FinProceso
