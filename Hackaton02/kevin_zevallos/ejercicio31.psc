Algoritmo ejercicio31
	Escribir "Calculando la media de los números pares e impares"
	Escribir "Ingrese diez números:"
	sumaPares <- 0
	sumaImpares <- 0
	cantPares <- 0
	cantImpares <- 0
	Para i <- 1 Hasta 10 Con Paso 1 hacer
		Leer numero
		Si numero MOD 2 = 0 Entonces
			sumaPares <- sumaPares + numero
			cantPares <- cantPares + 1
		SiNo
			sumaImpares <- sumaImpares + numero
			cantImpares <- cantImpares + 1
		FinSi
	FinPara
	Si cantPares > 0 Entonces
		mediaPares <- sumaPares / cantPares
		Escribir "La media de los números pares es:", mediaPares
	SiNo
		Escribir "No se ingresaron números pares"
	FinSi
	
	Si cantImpares > 0 Entonces
		mediaImpares <- sumaImpares / cantImpares
		Escribir "La media de los números impares es:", mediaImpares
	SiNo
		Escribir "No se ingresaron números impares"
	FinSi
	
FinAlgoritmo


