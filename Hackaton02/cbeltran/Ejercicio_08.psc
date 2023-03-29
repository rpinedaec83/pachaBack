Proceso Calcular_promedio

	nota1=0.0
	nota2=0.0
	nota3=0.0
	promedio=0.0
	
	Escribir "Ingrese la primera nota: "
	Leer nota1
	Escribir "Ingrese la segunda nota: "
	Leer nota2
	Escribir "Ingrese la tercera nota: "
	Leer nota3

	promedio = (nota1 + nota2 + nota3) / 3

	Escribir "El promedio de las notas es: ", promedio

	Si promedio >= 13 Entonces
		Escribir "El estudiante aprobó."
	Sino
		Escribir "El estudiante reprobó."
	FinSi
FinProceso
