Algoritmo Calculadora
	numero1 = 0;
	numero2 =0;
	operacion = "";
	resultado =0
	Escribir "Ingresa el primer numero";
	leer numero1;
	Escribir "Ingresa el segundo numero";
	Leer numero2;
	Escribir "Elige la operacion que deseas realizar (Suma(s), Resta(r), division(d), Multiplicacion(m)) ";
	Leer operacion;
	
		si operacion=="s" Entonces
			resultado=numero1 + numero2;
			Escribir "la suma de: " numero1 " mas " numero2 " es: " resultado;
		FinSi
	
		si operacion=="r" Entonces
			resultado=numero1 - numero2;
			Escribir "la resta de: " numero1 " menos " numero2 " es: " resultado;
		FinSi
	
		si operacion=="d" Entonces
			resultado=numero1 / numero2;
			Escribir "la division de: " numero1 " entre " numero2 " es: " resultado;
		FinSi
	
		si operacion=="m" Entonces
			resultado=numero1 * numero2;
			Escribir "la multiplicacion de: " numero1 " por " numero2 " es: " resultado;
		FinSi
	
	
	
	
FinAlgoritmo
