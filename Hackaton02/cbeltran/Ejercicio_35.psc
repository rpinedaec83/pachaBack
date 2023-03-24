Proceso Mayor_menor
	
	Escribir "Ingresa veinte números"
	mayor = -99999
	menor = 99999
	Para i = 1 Hasta 20 Con Paso 1 Hacer
		Escribir "Ingresa el número " i ": "
		Leer num
		Si num > mayor Entonces
			mayor = num
		FinSi
		Si num < menor Entonces
			menor = num
		FinSi
	FinPara
	Escribir "El número mayor es: " mayor
	Escribir "El número menor es: " menor
FinProceso
