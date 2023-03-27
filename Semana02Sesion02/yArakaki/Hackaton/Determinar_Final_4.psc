Algoritmo Determinar_Final_4
	// Declaración de variables
	numero1 = 0
	
	// Lectura del número
	Escribir "Ingrese un número: "
	Leer numero1
	
	// Verificación si termina en 4
	Si(numero1 MOD 10 = 4) Entonces
		Escribir("El número termina en 4")
	Sino
		Escribir("El número no termina en 4")
	FinSi
FinAlgoritmo