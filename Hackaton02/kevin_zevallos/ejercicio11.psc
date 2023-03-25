Algoritmo ejercicio11
    // Declarar variables
    Definir num1, num2, num3 Como Entero
	
    // Pedir al usuario que ingrese los números
    Escribir "Ingrese tres números: "
    Leer num1, num2, num3
	
    // Comparar los números
    Si num1 > num2 Y num1 > num3 Entonces
        Escribir "El número mayor es: ", num1
    SiNo Si num2 > num1 Y num2 > num3 Entonces
			Escribir "El número mayor es: ", num2
		SiNo
			Escribir "El número mayor es: ", num3
		FinSi
	FinSi
	
FinAlgoritmo

