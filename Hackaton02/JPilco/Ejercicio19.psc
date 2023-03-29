//Hacer un algoritmo en Pseint para una heladería se tienen 4 tipos de empleados ordenados de la siguiente forma con su número identificador y salario diario correspondiente:
//Cajero (56$/día).
//Servidor (64$/día).
//Preparador de mezclas (80$/día).
//Mantenimiento (48$/día).
//El dueño de la tienda desea tener un programa donde sólo ingrese dos números enteros que representen al número identificador del empleado y la cantidad de días que trabajó en la semana (6 días máximos). Y el programa le mostrará por pantalla la cantidad de dinero que el dueño le debe pagar al empleado que ingresó
Proceso Ejercicio19
	Escribir "Ingrese los numeros que representan al empreado "
	Leer tipo
	Escribir "Ingrese el numero de dias trabajados"
	leer diasTrabajados
	si diasTrabajados<=6 Entonces
		Segun tipo hacer
			01: Escribir "El monto total a pagar a un cajedo es de: ", (diasTrabajados*56)
			02: Escribir "El monto total a pagar a un cajedo es de: ", (diasTrabajados*64)
			03: Escribir "El monto total a pagar a un cajedo es de: ", (diasTrabajados*80)
			04: Escribir "El monto total a pagar a un cajedo es de: ", (diasTrabajados*48)
		FinSegun
	SiNo
		Escribir "El numero de dias exede a 6 ", diasTrabajados
	FinSi
	
FinProceso
