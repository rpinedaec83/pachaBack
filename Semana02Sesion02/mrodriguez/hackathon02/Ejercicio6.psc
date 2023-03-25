Algoritmo Ejercicio6
	//Hacer un algoritmo en Pseint para ayudar a un trabajador
	//a saber cual sera su sueldo semanal,
	//se sabe que si trabaja 40 horas o menos,
	//se le pagara $20 por hora,
	//pero si trabaja mas de 40 horas entonces
	//las horas extras se le pagaran a $25 por hora.

	Escribir "Numero de horas trabajadas: "
	leer horas

	si horas <= 40 Entonces
		Escribir "Pagar s/" (horas * 20)
	SiNo
		si horas > 40 Entonces
			Escribir "Pagar s/" (horas * 25)
		FinSi
	FinSi
FinAlgoritmo
