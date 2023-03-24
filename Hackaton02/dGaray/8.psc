Proceso sin_titulo
	Definir n1,n2,n3,prom Como Real
	Escribir "ingrese las notas del alumno del 0 al 20: "
    Leer nota1,nota2,nota3
    prom = (nota1+nota2+nota3)/3
    Escribir prom
	Si (prom>=13) Entonces
		Escribir "aprobado"
	SiNo
		Escribir "desaprobado"
	FinSi
FinProceso
