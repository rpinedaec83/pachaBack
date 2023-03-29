Algoritmo ejercicio_22
	Escribir "22. Hacer un algoritmo en Pseint para calcular la suma de los n primeros números."
	Definir  input Como Entero
	suma = 0
	contador = 1
	Escribir "Ingrese un numero para sumar sus predecesores:"
	Leer input
	Para contador=1 Hasta (input - 1) Hacer 
		suma = suma + contador
	FinPara
	
	Escribir "La suma de los predecesores es: ", suma
	
FinAlgoritmo
