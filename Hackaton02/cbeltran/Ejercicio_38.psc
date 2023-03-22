Proceso Numero_perfecto

    Escribir "Ingrese un número entero: "
    Leer n

    suma_divisores = 0
    
    para i = 1 hasta n-1 hacer
        si n mod i = 0 entonces
            suma_divisores = suma_divisores + i
        fin si
    fin para

    si suma_divisores = n entonces
        Escribir n " es un número perfecto."
    sino
        Escribir n " no es un número perfecto."
    fin si
FinProceso
