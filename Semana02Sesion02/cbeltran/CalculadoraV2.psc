Proceso CalculadoraV2
	numero1 = 0;
	numero2 =0;
	operacion = 0;
	resultado =0
	Escribir "Ingresa el primer numero";
	leer numero1;
	Escribir "Ingresa el segundo numero";
	Leer numero2;
	Escribir "Elige la operacion que deseas realizar"
	Escribir "Digita 1 para Sumar"
	Escribir "Digita 2 para Restar"
	Escribir "Digita 3 para Multiplicar"
	Escribir "Digita 4 para Dividir"
	Leer operacion;
	Segun operacion Hacer
		1:
			resultado=numero1 + numero2;
			Escribir "la suma de: " numero1 " mas " numero2 " es: " resultado;
		2:
			resultado=numero1 - numero2;
			Escribir "la resta de: " numero1 " menos " numero2 " es: " resultado;
		3:
			resultado=numero1 / numero2;
			Escribir "la division de: " numero1 " entre " numero2 " es: " resultado;
		4:
			resultado=numero1 * numero2;
			Escribir "la multiplicacion de: " numero1 " por " numero2 " es: " resultado;
			
		De Otro Modo:
			Escribir "Opcion no valida"
	FinSegun
		
	
FinProceso
