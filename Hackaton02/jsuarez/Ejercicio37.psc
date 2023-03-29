Funcion mcd_ <- mcdRecursivo (a, b)
	Si a < b Entonces
		mcd_ <- mcdRecursivo(b,a)
	SiNo
		Si b == 0 Entonces
			mcd_ <- a
		SiNo
			mcd_ <- mcdRecursivo(b,a%b)
		Fin Si
	Fin Si
	
Fin Funcion

Algoritmo MCD
	
	primerValor = 0
	segundoValor = 0
	Escribir "Inserta las valores para el MCD"
	Leer primerValor
	Leer segundoValor
	Escribir  mcdRecursivo(primerValor,segundoValor)
FinAlgoritmo
