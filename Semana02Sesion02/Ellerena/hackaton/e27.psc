Proceso e27
	
		Definir suma  Como Real 
		Definir contador Como Entero 
		Definir numero Como Real
		
		Escribir "Ingrese un número positivo (o un número negativo para salir): "
		Leer numero
		
		Mientras numero >= 0 Hacer
			suma <- suma + numero
			contador <- contador + 1
			Escribir "Ingrese otro número positivo (o un número negativo para salir): "
			Leer numero
		FinMientras
		
		Si contador > 0 Entonces
			media <- suma / contador
			Escribir "La media de los números ingresados es: ", media
		SiNo
			Escribir "No se ingresaron números positivos"
		FinSi
FinAlgoritmo


