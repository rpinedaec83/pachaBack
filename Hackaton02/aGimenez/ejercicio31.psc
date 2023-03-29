Proceso ejercicio31
	Definir contador, contadorPares, contadorImpares Como Entero
	Definir sumaPares, sumaImpares, numero1 Como Real
	numero1 = 1
	suma = 0
	contador = 0
	contadorImpares = 0
	contadorPares = 0
	
	Mientras contador <> 10 Hacer
		Escribir "Ingresa un numero"
		leer numero1
		si numero1 <> 0 Entonces
			si numero1 mod 2 == 0 Entonces
				sumaPares = sumaPares + numero1
				contadorPares = contadorPares + 1
			SiNo
				sumaImpares = sumaImpares + numero1
				contadorImpares = contadorImpares + 1
			FinSi
		FinSi
		contador = contador + 1
	FinMientras
	
	Escribir "La Suma de los Numeros Pares es: " sumaPares
	Escribir "Cantidad de Numeros Pares es: " contadorPares
	Escribir "El Promedio de Numeros Pares es: " sumaPares/contadorPares
	Escribir "--------------------------------------"
	Escribir "La Suma de los Numeros Impares es: " sumaImpares
	Escribir "Cantidad de Numeros Impares es: " contadorImpares
	Escribir "El Promedio de Numeros Impares es: " sumaImpares/contadorImpares
FinProceso
