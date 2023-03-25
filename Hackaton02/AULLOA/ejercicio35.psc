Algoritmo ejercicio35
	//Hacer un algoritmo en Pseint que nos permita saber cuál es el número mayor y menor, se debe ingresar sólo veinte números.
	Dimension Numeros_Ingresados[5]
	
	
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Leer Numeros_Ingresados[i]
	Fin Para
	numeroMayor = Numeros_Ingresados[1]
	numeroMenor = Numeros_Ingresados[1]
	
	
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Si Numeros_Ingresados[i] > numeroMayor  Entonces
			numeroMayor = Numeros_Ingresados[i]
		Fin Si
		
		Si Numeros_Ingresados[i] < numeroMenor  Entonces
			numeroMenor = Numeros_Ingresados[i]
		Fin Si
		
	Fin Para
	
	
	Escribir numeroMayor
	Escribir numeroMenor
FinAlgoritmo
	
