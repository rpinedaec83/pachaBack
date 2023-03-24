Algoritmo ejer16
	//Hacer un algoritmo en Pseint que lea un número y según ese número, indique el día que corresponde.
	// Declarar la variable
     num_dia =0
    
    // Leer el número del día por teclado
    Escribir "Introduce el número del día:" 
    Leer num_dia 
    
    // Determinar el día correspondiente según el número ingresado
    Segun num_dia Hacer
        1: Escribir "El número ", num_dia, " corresponde al día Lunes" 
        2: Escribir "El número ", num_dia, " corresponde al día Martes" 
        3: Escribir "El número ", num_dia, " corresponde al día Miércoles" 
        4: Escribir "El número ", num_dia, " corresponde al día Jueves" 
        5: Escribir "El número ", num_dia, " corresponde al día Viernes"
        6: Escribir "El número ", num_dia, " corresponde al día Sábado"
        7: Escribir "El número ", num_dia, " corresponde al día Domingo"
        De Otro Modo: Escribir "El número ingresado no es válido" 
    FinSegun
	
FinAlgoritmo
