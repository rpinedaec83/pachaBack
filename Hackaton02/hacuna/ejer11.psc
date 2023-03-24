Algoritmo MayorDeTresNumeros
	
    // Pedir al usuario los tres números
    Escribir "Ingrese el primer número: "
    Leer numero1
    Escribir "Ingrese el segundo número: "
    Leer numero2
    Escribir "Ingrese el tercer número: "
    Leer numero3
	
    // Comparar los tres números y determinar cuál es el mayor
    Si numero1 > numero2 Y numero1 > numero3 Entonces
        mayor <- numero1
    SiNo Si numero2 > numero3 Entonces
			mayor <- numero2
		SiNo
			mayor <- numero3
		FinSi
	FinSi
		
		// Mostrar el resultado
		Escribir "El número mayor es: ", mayor
	
		
FinAlgoritmo

