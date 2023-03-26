Algoritmo PoblacionMasPersonas
	
	Dimension PersonasXCiudad[11]
	Ciudad_Mas_Habitantes = 0
	Para i<-1 Hasta 11 Con Paso 1 Hacer
		Leer PersonasXCiudad[i]
		
		Si PersonasXCiudad[i] > Ciudad_Mas_Habitantes  Entonces
			Ciudad_Mas_Habitantes = PersonasXCiudad[i]
		Fin Si
		
	Fin Para
	
	Escribir "La ciudad con mas habitantes tiene ", Ciudad_Mas_Habitantes, " habitantes"
	
FinAlgoritmo
