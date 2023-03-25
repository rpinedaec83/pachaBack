Proceso Ejercicio8
	
	Definir nota1, nota2, nota3, promedio Como Real;
	promedio <- 0;
	
	Escribir "Recuerda que la mínima nota aprobatoria es 12";
	Escribir "Ingresar sus 3 notas:";
	Leer nota1, nota2, nota3;
	
	promedio <- (nota1 + nota2 + nota3) / 3;
	
	si (promedio >= 11.5) entonces
		Escribir " Estudiante Aprobado";
	SiNo
		Escribir "Estudiante Reprobado";
	FinSi
	
FinProceso
