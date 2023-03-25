Algoritmo Media_DiezNumeros
	Dimension array[10]
	numeroAcumulado_Par = 0
	pares = 0
	numeroAcumulado_Impar = 0
	impares = 0
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Leer array[i]
		Si array[i]%2==0 Entonces
			numeroAcumulado_Par = numeroAcumulado_Par + array[i]
			pares = pares + 1
		SiNo
			numeroAcumulado_Impar = numeroAcumulado_Impar + array[i]
			impares = impares +1
		Fin Si


	Fin Para
	
	Escribir  "Media de pares: " numeroAcumulado_Par/pares
	Escribir  "Media de impares: " numeroAcumulado_Impar/impares
	
FinAlgoritmo
