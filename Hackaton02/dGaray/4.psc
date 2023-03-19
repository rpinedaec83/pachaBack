Proceso sin_titulo
	Escribir "Ingrese un numero"
	leer numero1
	Escribir "Ingrese un numero"
	leer numero2
	Escribir "Ingrese un numero"
	leer numero3

	si numero1 > numero2 Entonces
		Si numero2 > numero3 Entonces
			Escribir "El orden seria ", numero3, ", ",numero2,", ",numero1
		SiNo
			Si numero1 > numero3 Entonces
				Escribir "El orden seria ", numero2, ", ",numero3,", ",numero1
			SiNo
				Escribir "El orden seria ", numero2, ", ",numero1,", ",numero3
			FinSi
		FinSi
	SiNo
		Si numero1 > numero3 Entonces
			Escribir "El orden seria ", numero3, ", ",numero1,", ",numero2
		SiNo
			Si numero2 > numero3 Entonces
				Escribir "El orden seria ", numero1, ", ",numero3,", ",numero2
			SiNo
				Escribir "El orden seria ", numero1, ", ",numero2,", ",numero3
			FinSi
		FinSi
	FinSi
FinProceso

