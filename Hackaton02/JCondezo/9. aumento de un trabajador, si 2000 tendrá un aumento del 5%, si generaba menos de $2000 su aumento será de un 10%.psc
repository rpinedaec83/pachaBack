// determinar el aumento de un trabajador, 
//se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%, si generaba menos de 
//		$2000 su aumento será de un 10%.

Algoritmo sin_titulo
	Escribir "Ingresa el valor de sueldo:";
    Leer sueldo;
    incremento <- 0;
    Si sueldo<2000 Entonces
        incremento <- sueldo*0.10;
    FinSi
    Si sueldo>=2000 
        incremento <- sueldo*0.05;
    FinSi
    nuevo_sueldo <- sueldo+incremento;
    Escribir "EL sueldo se incremento en: ", incremento;
    Escribir "Su nuevo sueldo es de: ", nuevo_sueldo;
	
FinAlgoritmo
