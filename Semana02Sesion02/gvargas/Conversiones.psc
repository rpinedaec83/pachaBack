Algoritmo Conversiones
	medicion = ""
	cant = 0
	conver = 0
	Escribir "Escriba al tipo de medición que quiere convertir (p) a pulgadas (k) a kilogramos: "
	Leer medicion
	Si medicion = "p" Entonces
		Escribir "Indique los centímetros: "
		Leer cant
		conver = cant/2.54
		Escribir cant " centímetros es igual a " conver " pulgadas"
	SiNo
		Si medicion = "k" Entonces
			Escribir "Indique las libras: "
			Leer cant
			conver = cant/2.205
			Escribir cant " libras es igual a " conver " kilogramos"
		SiNo
			Escribir "Opción no válida"
		FinSi
	FinSi
FinAlgoritmo
