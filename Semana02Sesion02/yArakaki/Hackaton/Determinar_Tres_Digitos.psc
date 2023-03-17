Algoritmo Determinar_Tres_Digitos
	// Declaración de variables
	numero1 = 0
	
	// Lectura del número
	Escribir("Ingrese un número: ")
	Leer numero1
	
	// Verificación de tres dígitos
	Si(numero >= 100 Y numero <= 999) Entonces
		Escribir("El número tiene tres dígitos")
	Sino
		Escribir("El número no tiene tres dígitos")
	FinSi
FinAlgoritmo