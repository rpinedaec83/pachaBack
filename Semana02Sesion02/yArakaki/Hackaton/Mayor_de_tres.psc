Algoritmo Mayor_de_tres
	
	
	Definir numero1, numero2, numero3, mayor como Entero
	
	
	Escribir "Ingrese el primer número:"
	Leer numero1
	Escribir "Ingrese el segundo número:"
	Leer numero2
	Escribir "Ingrese el tercer número:"
	Leer numero3
	
	
	Si numero1 >= numero2 y numero1 >= numero3 Entonces
		mayor <- numero1
	Sino Si numero2 >= numero1 y numero2 >= numero3 Entonces
			mayor <- numero2
		Sino
			mayor <- numero3
		FinSi
	FinSi	
		
		Escribir "El número mayor es: " , mayor
		
FinAlgoritmo
