Algoritmo ejercicio8
    // Declarar variables
    Definir salario, aumento Como Real
	
    // Pedir salario
    Escribir "Ingrese el salario del trabajador: "
    Leer salario
	
    // Determinar el aumento
    Si salario > 2000 Entonces
        aumento = salario * 0.05
    SiNo
        aumento = salario * 0.1
    FinSi
	
    // Mostrar el nuevo salario con el aumento
    salario = salario + aumento
    Escribir "El nuevo salario del trabajador es: ", salario
	
FinAlgoritmo