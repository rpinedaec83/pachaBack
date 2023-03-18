Proceso e8
	
    Definir salario, aumento, nuevo_salario Como Real
    
    Escribir "Ingrese el salario del trabajador:"
    Leer salario
    
    Si salario >= 2000 Entonces
        aumento <- salario * 0.05
    Sino
        aumento <- salario * 0.1
    FinSi
    
    nuevo_salario <- salario + aumento
    
    Escribir "El nuevo salario del trabajador es:", nuevo_salario
FinAlgoritmo