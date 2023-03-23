Proceso Ejercicio18
	Definir cantidadCD Como Real
    Definir precioTotal Como Real
    Escribir "Introduce la cantidad de CDs a vender:";
    Leer cantidadCD
	
    Si cantidadCD < 10 Entonces
        precioTotal = 10 * cantidadCD
    Sino
        Si cantidadCD >= 10 Y cantidadCD <= 99 Entonces
            precioTotal = 8 * cantidadCD
        Sino
            Si cantidadCD >= 100 Y cantidadCD <= 499 Entonces
                precioTotal = 7 * cantidadCD
            Sino
                precioTotal = 6 * cantidadCD
            FinSi
        FinSi
    FinSi
	
    Escribir "El precio total para el cliente es: $",precioTotal
    Escribir "La ganancia para el vendedor es: $",precioTotal* 0.0825
FinProceso
