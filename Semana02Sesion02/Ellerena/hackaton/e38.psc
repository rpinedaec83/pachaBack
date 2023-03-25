Algoritmo e38
    Definir num, suma, i Como Entero
    
    Escribir "Ingrese un número: "
    Leer num
    
    suma <- 0
    
    Para i <- 1 Hasta num/2 Con Paso 1 Hacer
        Si num Mod i = 0 Entonces
            suma <- suma + i
        FinSi
    FinPara
    
    Si suma = num Entonces
        Escribir "El número ingresado es un número perfecto."
    SiNo
        Escribir "El número ingresado no es un número perfecto."
    FinSi
    
FinAlgoritmo
