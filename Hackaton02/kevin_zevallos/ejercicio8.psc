Algoritmo ejercicio8
    // Declarar variables
    Definir nota1, nota2, nota3, promedio Como Real
	
    // Pedirlas tres notas
    Escribir "Ingrese la primera nota: "
    Leer nota1
    Escribir "Ingrese la segunda nota: "
    Leer nota2
    Escribir "Ingrese la tercera nota: "
    Leer nota3
	
    // Calcular el promedio
    promedio = (nota1 + nota2 + nota3) / 3
	
    // Determinar si el estudiante aprobó o no
    Si promedio >= 10.5 Entonces
        Escribir "El estudiante aprobó con un promedio de: ", promedio
    SiNo
        Escribir "El estudiante no aprobó con un promedio de: ", promedio
    FinSi
	
FinAlgoritmo
