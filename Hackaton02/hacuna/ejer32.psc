Algoritmo CiudadMasPoblada
	
	Definir provincia, ciudad, poblacion, max_poblacion como cadena
	Definir maximo como entero
	
	maximo <- 0
	
	Para i<-1 Hasta 3 Con Paso 1 Hacer
		Escribir("Ingrese el nombre de la provincia ",i)
		Leer(provincia)
		Para j<-1 Hasta 11 Con Paso 1 Hacer
			Escribir("Ingrese el nombre de la ciudad ",j," de la provincia ",provincia)
			Leer(ciudad)
			Escribir("Ingrese la población de la ciudad ",ciudad," de la provincia ",provincia)
			Leer(poblacion)
			Si poblacion > maximo Entonces
				maximo <- poblacion
				max_poblacion <- ciudad
			FinSi
		FinPara
	FinPara
	
	Escribir("La ciudad con la población más alta es ", max_poblacion, " con ", maximo, " personas.")
	
FinAlgoritmo


