Algoritmo ejercicio04
	Escribir "Ingrese los numeros"
	leer num1
	leer num2
	leer num3
	si num1 < num2 y num1 < num3 entonces
		menor <- num1
		si num2 < num3 entonces
			medio <- num2
			mayor <- num3
		sino
			medio <- num3
			mayor <- num2
		fin si
	sino si num2 < num1 y num2 < num3 entonces
		menor <- num2
		si num1 < num3 entonces
			medio <- num1
			mayor <- num3
		sino
			medio <- num3
			mayor <- num1
		fin si
		sino
			menor <- num3
			si num1 < num2 entonces
				medio <- num1
				mayor <- num2
			sino
				medio <- num2
				mayor <- num1
			fin si
		fin si
	fin si
	escribir "Los números en orden ascendente son: ", menor, ", ", medio, ", ", mayor
FinAlgoritmo
