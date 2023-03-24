Proceso ejercicio04
	numero1 = 0
	numero2 = 0
	numero3 = 0
	
	Escribir "Ingrese un numero"
	Leer numero1
	Escribir "Ingrese otro numero"
	Leer numero2 
	Escribir "Ingrese ultimo numero"
	Leer numero3
	
	Escribir "Numeros de Menor a Mayor"
	si numero1 < numero2 y numero1 < numero3 Entonces
		Escribir "El menor es: " numero1
	FinSi
	si numero2 < numero1 y numero2 < numero3 Entonces
		Escribir "El menor es: " numero2
	FinSi
	si numero3 < numero1 y numero3 < numero2 Entonces
		Escribir "El menor es: " numero3
	FinSi
	
	si numero1 < numero2 y numero1 > numero3 Entonces
		Escribir "El del medio es: " numero1
	FinSi
	si numero2 > numero1 y numero2 < numero3 Entonces
		Escribir "El del medio es: " numero2
	FinSi
	si numero3 < numero1 y numero3 > numero2 Entonces
		Escribir "El del medio es: " numero3
	FinSi
	
	si numero1 > numero2 y numero1 > numero3 Entonces
		Escribir "El mayor es: " numero1
	FinSi
	si numero2 > numero1 y numero2 > numero3 Entonces
		Escribir "El mayor es: " numero2
	FinSi
	
	si numero3 > numero1 y numero3 > numero2 Entonces
		Escribir "El mayor es: " numero3
	FinSi
FinProceso
