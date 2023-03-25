Proceso  Ejercicio27
    Definir suma, contador, numero Como Real
    suma = 0
    contador = 0
    Escribir "Introduce un número positivo (o un número negativo para terminar): "
    Leer numero;
    Mientras numero >= 0 Hacer
        suma = suma + numero
        contador = contador + 1
        Escribir "Introduce otro número positivo (o un número negativo para terminar): "
        Leer numero
    FinMientras
    Si contador > 0 Entonces
        Escribir "La media es: ", suma/contador
    Sino
        Escribir "No se han introducido números válidos"
    FinSi
FinProceso
