Algoritmo AumentoTrabajador
	
    // Pedir al usuario el sueldo del trabajador
    Escribir "Ingrese el sueldo del trabajador: "
    Leer sueldo
	
    // Determinar el porcentaje de aumento según el sueldo
    Si sueldo > 2000 Entonces
        porcentajeAumento <- 0.05
    SiNo
        porcentajeAumento <- 0.1
    FinSi
	
    // Calcular el aumento y el nuevo sueldo
    aumento <- sueldo * porcentajeAumento
    nuevoSueldo <- sueldo + aumento
	
    // Mostrar el resultado
    Escribir "El sueldo original es: $", sueldo
    Escribir "El porcentaje de aumento es: ", porcentajeAumento * 100, "%"
    Escribir "El aumento es: $", aumento
    Escribir "El nuevo sueldo es: $", nuevoSueldo
	
FinAlgoritmo

