Proceso Ejercicio19
	Definir idEmpleado, diasTrabajados Como Entero;
    Escribir "Introduce el número identificador del empleado:";
	Escribir  "1. Cajero"
	Escribir  "2. Servidor"
	Escribir  "3. Preparador de mezclas"
	Escribir  "4. Mantenimiento"
    Leer idEmpleado;
    Escribir "Introduce la cantidad de días trabajados:";
    Leer diasTrabajados;
		
	Si diasTrabajados > 6 Entonces
		Escribir "6 días máximos de trabajo";
	Sino
		Segun idEmpleado Hacer
			1: Escribir "El salario a pagar al empleado es: $",56*diasTrabajados;
			2: Escribir "El salario a pagar al empleado es: $",64*diasTrabajados;
			3: Escribir "El salario a pagar al empleado es: $",80*diasTrabajados;
			4: Escribir "El salario a pagar al empleado es: $",48*diasTrabajados;
			De Otro Modo:
				Escribir "Número identificador de empleado inválido";
		FinSegun
	FinSi
FinProceso
