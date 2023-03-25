Algoritmo suma_impares
	
	Definir n, i, suma Como Entero
	
	Escribir "Ingrese un número entero positivo: "
	Leer n
	
	suma = 0
	
	Para i = 1 Hasta n Hacer
		Si i % 2 = 1 Entonces
			suma = suma + i
		FinSi
	FinPara
	
	Escribir "La suma de los números impares menores o iguales a ", n, " es: ", suma
	
FinAlgoritmo

