Algoritmo Mayor_de_dos_numeros
	
	Definir numero1, numero2, mayor como Entero
	
	
	Escribir "Ingrese el primer número:"
	Leer numero1
	Escribir "Ingrese el segundo número:"
	Leer numero2
	
	
	Si numero1 >= numero2 Entonces
		mayor <- numero1
	Sino
		mayor <- numero2
	FinSi
	
	// Mostrar el número mayor
	Escribir "El número mayor es: " , mayor
	
FinAlgoritmo
