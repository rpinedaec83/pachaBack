Proceso Aprobacion_curso
	Nota1  = 0
	Nota2  = 0
	Nota3  = 0
	promedio = 0
	
	escribir "Ingresa Nota1: "
	leer Nota1
	escribir "Ingresa Nota2: "
	leer Nota2
	escribir "Ingresa Nota3: "
	leer Nota3
	
	promedio = (Nota1 + Nota2 + Nota3)/3
	
	Si promedio >= 11 entonces
		Escribir "Alumno aprobado"
	sino escribir "Alumno desaprobado"
	FinSi
	
FinProceso
