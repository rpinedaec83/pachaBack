Algoritmo ejer28
	Definir  cantidadNumeros <= 0
    Entero sumaNumeros <- 0
    Real numero
    
    // Ciclo para ingresar los números
    Mientras Verdadero
        Escribir "Ingrese un número positivo o un número negativo para terminar: "
        Leer numero
        Si numero >= 0 Entonces
            cantidadNumeros <- cantidadNumeros + 1
            sumaNumeros <- sumaNumeros + numero
        Sino
            Salir
        FinSi
    FinMientras
    
    // Cálculo de la media
    Si cantidadNumeros > 0 Entonces
        Real media <- sumaNumeros / cantidadNumeros
        Escribir "La media de los números ingresados es: ", media
    Sino
        Escribir "No se ingresó ningún número positivo."
    FinSi
FinAlgoritmo
