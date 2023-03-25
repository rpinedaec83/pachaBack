Algoritmo sin_titulo
//8.-Hacer un algoritmo en Pseint para calcular el promedio de tres notas y determinar si el estudiante aprobó o no.
			
		promedio <- 0;
		
		Escribir "Recuerda que la mínima nota aprobatoria es 11";
		Escribir "Ingresar sus 3 notas:";
		Leer nota1, nota2, nota3;
		
		promedio <- (nota1 + nota2 + nota3) / 3;
		
		si (promedio >= 10.5) entonces
			Escribir " Estudiante Aprobado";
		SiNo
			Escribir "Estudiante Desaprobado";
		FinSi
		

FinAlgoritmo
