Algoritmo ejercicio6
    // Declarar variables
    Definir horas_trabajadas, sueldo_base, sueldo_extra, sueldo_total Como Real
	
    // Pedir al usuario que ingrese las horas trabajadas
    Escribir "Ingrese las horas trabajadas esta semana: "
    Leer horas_trabajadas
	
    // Calcular el sueldo base y el sueldo extra
    Si horas_trabajadas <= 40 Entonces
        sueldo_base = horas_trabajadas * 20
        sueldo_extra = 0
    SiNo
        sueldo_base = 40 * 20
        sueldo_extra = (horas_trabajadas - 40) * 25
    FinSi
	
    // Calcular el sueldo total
    sueldo_total = sueldo_base + sueldo_extra
	
    // Mostrar el resultado
    Escribir "Su sueldo base es de: $", sueldo_base
    Escribir "Su sueldo extra es de: $", sueldo_extra
    Escribir "Su sueldo total es de: $", sueldo_total
	
FinAlgoritmo

