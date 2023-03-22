Proceso Ejercicio37
	Escribir "Introduce un número: "
    Leer n
    suma <- 0
    Para i <- 1 Hasta n/2 Con Paso 1 Hacer
        Si n mod i = 0 Entonces
            suma <- suma + i
        FinSi
    FinPara
    Si suma = n Entonces
        Escribir n, " si es perfecto"
    SiNo
        Escribir n, " no es perfecto"
    FinSi
FinProceso
