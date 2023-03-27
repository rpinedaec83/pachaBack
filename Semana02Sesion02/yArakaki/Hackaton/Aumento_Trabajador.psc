Algoritmo Aumento_Trabajador
	
	
	Definir salario como Real
	Definir aumento como Real
	
	
	Escribir "Ingrese el salario actual del trabajador:"
	Leer salario
	
	
	Si salario > 2000 Entonces
		aumento <- salario * 0.05
	Sino
		aumento <- salario * 0.1
	FinSi
	
	
	Escribir "El aumento correspondiente es: $" , aumento
	
FinAlgoritmo
