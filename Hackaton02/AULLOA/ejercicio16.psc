Algoritmo ejercicio16
	//Hacer un algoritmo en Pseint donde se ingrese una hora y nos calcule la hora dentro de un segundo.
	Definir hh,mm,ss Como Entero

	Escribir "Ingrese hh,mm,ss"
	Leer hh
	Leer mm
	Leer ss
	
	Si	hh < 24 y mm < 60 y ss < 60 Entonces
		ss <- ss + 1
		Si(ss = 60)
			ss <- 0
			mm <- mm + 1
			Si (mm = 60) Entonces
				mm <- 0
				hh <- hh + 1
				Si (hh = 24) Entonces
					hh <- 0
				FinSi
			FinSi
		FinSi
	FinSi
	
	Escribir hh, " : ", mm, " : ", ss
	
FinAlgoritmo