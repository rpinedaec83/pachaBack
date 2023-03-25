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
//ejercicio37 Hacer un algoritmo en Pseint para conseguir el M.C.D de un número por medio del algoritmo de Euclides.
	Escribir  mcdRecursivo(1,12)
FinAlgoritmo
	
