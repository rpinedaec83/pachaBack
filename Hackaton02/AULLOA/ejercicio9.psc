Algoritmo ejercicio9
	//Hacer un algoritmo en Pseint para determinar el aumento de un trabajador, se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%, si generaba menos de $2000 su aumento será de un 10%.
	Escribir Sin Saltar "Ingresa el valor de sueldo:";
    Leer sueldo;
    incremento <- 0;
    Si sueldo>2000 Entonces
        incremento <- sueldo*0.05;
    FinSi
    Si sueldo<2000 Entonces
        incremento <- sueldo*0.1;
    FinSi
    nuevo_sueldo <- sueldo+incremento;
    Escribir "Valor de incremento: ", incremento;
    Escribir "Valor de nuevo sueldo: ", nuevo_sueldo;
FinAlgoritmo