//para calcular el promedio de tres notas y determinar
//si el estudiante aprobó o no.
Algoritmo sin_titulo
    Escribir "Ingrese Nota 1 : "
    Leer Nota1
    Escribir "Ingrese Nota 2 : "
    Leer Nota2
    Escribir "Ingrese Nota 3 : "
    Leer Nota3
    promedio = (Nota1+Nota2+Nota3)/3
    Escribir "EL PROMEDIO ES : ", promedio
	si promedio>=10 Entonces
		Escribir "al alumno aprobo"
	sino 
		escribir "el alumno ha desaprobado"
	FinSi
FinAlgoritmo 