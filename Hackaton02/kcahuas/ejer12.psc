Algoritmo ejer12
	Escribir "Escriba un numero: ";
    Leer Numero1;
    
    Escribir "Escriba otro numero: ";
    Leer Numero2;
    
    // Determinar mediante condiciones cual es el número mayor
    Si (Numero1 > Numero2) Entonces
        NumeroMayor <- Numero1;
    Sino
        NumeroMayor <- Numero2;
    FinSi
    
    Escribir "El numero mayor es: ", NumeroMayor;
FinAlgoritmo
