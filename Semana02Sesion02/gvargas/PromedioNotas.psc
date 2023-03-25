Algoritmo PromedioNotas
	nota1 = 0
	nota2 = 0
	nota3 = 0
	prom = 0
	Escribir "Escriba la primera nota: "
	Leer nota1
	Escribir "Escriba la segunda nota: "
	Leer nota2
	Escribir "Escriba la tercera nota: "
	Leer nota3
	prom = (nota1 + nota2 + nota3)/3
	Si prom >= 10.5 Entonces
		Escribir "El estudiante aprobó el curso con: " prom
	SiNo
		Escribir "El estudiante desaprobó el curso con: " prom
	FinSi
FinAlgoritmo
